import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone

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

        #matchIndex=np.argmin(faceDis) #current change
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