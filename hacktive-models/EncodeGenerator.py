import pymongo
import urllib.request
from PIL import Image
import cv2
import face_recognition
import pickle

client = pymongo.MongoClient("mongodb+srv://FinalDatabase:HyperHactive@cluster0.xdhqnvi.mongodb.net/FinalDatabase?retryWrites=true&w=majority")
cursor2=client.FinalDatabase.Final.find({},{'_id':0,'RegNo':1})
print(cursor2)
# Database Name
# db = client.FinalDatabase
# # Collection Name
# col = db.Final
# x = col.find_one({'_id':1})
regno=211081010 #from QR
#IMPORTANT : Dictionary pattern for ref 
#{'_id': 1, 'RegNo': 211080001, 'Name': 'Samarth Gupta', 'Photo': 'https://surveyheartmedia.s3.ap-south-1.amazonaws.com/files/7f505e0951dc0254d2efcfde04d2ff/63d5d78a910004541035906d/sh_1674977540527.jpg'}
cursor=client.FinalDatabase.Final.find_one({'RegNo':regno})
print(cursor)
img_link=cursor['Photo']  
urllib.request.urlretrieve(img_link,"img.png") 
#img = Image.open("gfg.png")
#img.show()
image1 = face_recognition.load_image_file("img.png")

# black_link="https://images.unsplash.com/photo-1603366615917-1fa6dad5c4fa?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGxhaW4lMjBibGFja3xlbnwwfHwwfHw%3D&w=1000&q=80"
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