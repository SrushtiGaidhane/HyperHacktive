import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
import numpy as np
from pyzbar.pyzbar import decode
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance-20d3c-default-rtdb.firebaseio.com/"
})
 
ref = db.reference('Students')
 
data = {
    "211081000":
        {
            "name": "Mikhil Angre",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "211081002":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "211081004":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}
 
for key, value in data.items():
    ref.child(key).set(value)
    
lis = list(ref.get().keys())

# ------------------------------------------------------------------------------------------------------
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
     
    success,img  = cap.read()
    for qrcode in decode(img):
        tempmyData = qrcode.data.decode('utf-8')
        myData = tempmyData[4:]
        # print(myData)

        for i in range(len(lis)):
            if(myData == lis[i]):
                print('Match Found ')
            else:
                print('Bhak')
                break

        pts = np.array(qrcode.polygon,np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)

        pts2 = qrcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,
                    0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(5)

    