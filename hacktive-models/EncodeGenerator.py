import pymongo
import urllib.request
from PIL import Image
# import cv2
import face_recognition
import pickle
# import os
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import  storage

# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': "https://faceattendance-20d3c-default-rtdb.firebaseio.com/",
#     'storageBucket': "faceattendance-20d3c.appspot.com"
# })


client = pymongo.MongoClient("mongodb+srv://FinalDatabase:HyperHactive@cluster0.xdhqnvi.mongodb.net/FinalDatabase?retryWrites=true&w=majority")
# Database Name
# db = client.FinalDatabase
# # Collection Name
# col = db.Final
# x = col.find_one({'_id':1})
regno=211081030 #from QR
#IMPORTANT : Dictionary pattern for ref 
#{'_id': 1, 'RegNo': 211080001, 'Name': 'Samarth Gupta', 'Photo': 'https://surveyheartmedia.s3.ap-south-1.amazonaws.com/files/7f505e0951dc0254d2efcfde04d2ff/63d5d78a910004541035906d/sh_1674977540527.jpg'}
cursor=client.FinalDatabase.Final.find_one({'RegNo':regno})
#print(x,type(x))
img_link=cursor['Photo']  
urllib.request.urlretrieve(img_link,"img.png") 
#img = Image.open("gfg.png")
#img.show()
image1 = face_recognition.load_image_file("img.png")


# image1_encoding = face_recognition.face_encodings(image1)[0]
# print(image1_encoding) 

# image2 = face_recognition.load_image_file("D:\My Documents\Desktop\WIN_20201206_15_20_00_Pro.jpg")
# image2_encoding = face_recognition.face_encodings(image2)[0]
# print(image2_encoding) 
# print("img1 and img2 both encodings generated")
#we use [0] to grab the first person’s Face Encoding’s. 
#By default we assume that there are more than one person in the image

def findEncodings(img):
    encode = face_recognition.face_encodings(img)[0]
    return encode

studentIds=[]
studentIds.append(regno)
print("Encoding ...")
encodeListKnown = findEncodings(image1)
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