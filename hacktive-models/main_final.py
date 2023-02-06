import cv2
import numpy as np
from pyzbar.pyzbar import decode
import pymongo
import urllib.request
import face_recognition
import pickle
import os
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

camera_id = 0
delay = 1
window_name = 'OpenCV pyzbar'

cap = cv2.VideoCapture(camera_id)
flag = 0

while (flag == 0):
    ret, frame = cap.read()

    if ret:
        for d in decode(frame):
            s = d.data.decode()
            # print(s)

            global reg_id
            reg_id = s
                
            if(s != ''):
                flag = 1
                
            frame = cv2.rectangle(frame, (d.rect.left, d.rect.top),
                                  (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)
            frame = cv2.putText(frame, s, (d.rect.left, d.rect.top + d.rect.height),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)

print(reg_id)

client = pymongo.MongoClient("mongodb+srv://FinalDatabase:HyperHactive@cluster0.xdhqnvi.mongodb.net/FinalDatabase?retryWrites=true&w=majority")
cursor1=client.FinalDatabase.Final.find({},{'_id':0,'RegNo':1})
for x in cursor1:
    if x['RegNo'] == int(reg_id):
        print('Approved')
        break
#--------------------QR code ends----------------------
#--------------------Encode generation starts----------
#client = pymongo.MongoClient("mongodb+srv://FinalDatabase:HyperHactive@cluster0.xdhqnvi.mongodb.net/FinalDatabase?retryWrites=true&w=majority")
# Database Name
# db = client.FinalDatabase
# # Collection Name
# col = db.Final
# x = col.find_one({'_id':1})
#regno=211081010 #from QR
regno=int(reg_id) #from QR
#IMPORTANT : Dictionary pattern for ref 
#{'_id': 1, 'RegNo': 211080001, 'Name': 'Samarth Gupta', 'Photo': 'https://surveyheartmedia.s3.ap-south-1.amazonaws.com/files/7f505e0951dc0254d2efcfde04d2ff/63d5d78a910004541035906d/sh_1674977540527.jpg'}
cursor=client.FinalDatabase.Final.find_one({'RegNo':regno})
print(cursor)
img_link=cursor['Photo']  
urllib.request.urlretrieve(img_link,"img.png") 
#img = Image.open("gfg.png")
#img.show()
image1 = face_recognition.load_image_file("img.png")

black_link="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Elon_Musk_Royal_Society_%28crop2%29.jpg/1200px-Elon_Musk_Royal_Society_%28crop2%29.jpg"
urllib.request.urlretrieve(black_link,"black.png") 
black =  face_recognition.load_image_file("black.png")

# image1_encoding = face_recognition.face_encodings(image1)[0]
# print(image1_encoding) 

# image2 = face_recognition.load_image_file("D:\My Documents\Desktop\WIN_20201206_15_20_00_Pro.jpg")
# image2_encoding = face_recognition.face_encodings(image2)[0]
# print(image2_encoding) 
# print("img1 and img2 both encodings generated")
#we use [0] to grab the first person’s Face Encoding’s. 
#By default we assume that there are more than one person in the image

# def findEncodings(img):
#     encode = face_recognition.face_encodings(img)[0]
#     return encode
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #print(type(img))
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


studentIds=[]
studentIds.append(regno)
studentIds.append(0)
image_list=[]
image_list.append(image1)
image_list.append(black)
print("Encoding ...")
encodeListKnown = findEncodings(image_list)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")



# print(x)
# for data in x:
# print(data)
# print(x)
 

# Importing student images
# folderPath = 'Images'
# pathList = os.listdir(folderPath)
# print(pathList)
# imgList = []
# studentIds = []
# for path in pathList:
#     imgList.append(cv2.imread(os.path.join(folderPath, path)))
#     studentIds.append(os.path.splitext(path)[0])

#     fileName = f'{folderPath}/{path}'
#     bucket = storage.bucket()
#     blob = bucket.blob(fileName)
#     blob.upload_from_filename(fileName)


#     # print(path)
#     # print(os.path.splitext(path)[0])
# print(studentIds)

# def findEncodings(imagesList):
#     encodeList = []
#     for img in imagesList:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)

#     return encodeList


# print("Encoding Started ...")
# encodeListKnown = findEncodings(imgList)
# encodeListKnownWithIds = [encodeListKnown, studentIds]
# print("Encoding Complete")

# file = open("EncodeFile.p", 'wb')
# pickle.dump(encodeListKnownWithIds, file)
# file.close()
# print("File Saved")

#---------------------Encode Generator ends------------------
#---------------------UI and image capturing starts-------------
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 350)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

imgBackground=cv2.imread("Resources/11.jpeg")

#Importing the mode images into a list
folderModePath="Resources/Modes"
modePathList=os.listdir(folderModePath)
imgModeList=[]
#print(modePathList)
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
#print(len(imgModeList))

#import encoding file
with open("EncodeFile.p","rb") as myfile:
    encodeListwithIds=pickle.load(myfile)
known,ids=encodeListwithIds
print(ids)

while (True):
    success, img=cap.read()
    smallimg=cv2.resize(img,(330,330),None,0.25,0.25)
    smallimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    facecurrent=face_recognition.face_locations(smallimg)
    encodecurface=face_recognition.face_encodings(smallimg,facecurrent)
    
    imgBackground[202:202+288,48:48+352]=img
    #imgBackground[490:490+139,56:56+248]=imgModeList[1]

    for eFace,faceLoc in zip(encodecurface,facecurrent):
        matches=face_recognition.compare_faces(known,eFace)
        faceDis=face_recognition.face_distance(known,eFace)
        print("matches",matches)
        print("faceDis",faceDis)

        matchIndex=np.argmin(faceDis) #current change
        print("Match Index",matchIndex)

        if(matches[matchIndex]):
            print("DETECTED !")
            imgBackground[490:490+139,56:56+248]=imgModeList[0]
            #y1,x2,y2,x1=faceLoc
            #y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            #bbox=55+x1,162+y1,x2-x1,y2-y1
            #imgBackground=cvzone.cornerRect(imgBackground,bbox,rt=0)
        else:
            imgBackground[490:490+139,56:56+248]=imgModeList[1]
    #cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance",imgBackground)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#---------------------------UI and image capturing ends---------------