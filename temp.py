import json
import  pymongo
from pymongo import MongoClient, InsertOne
# with open("data.json") as f:
#     output=json.load(f)
# print(output)

client = pymongo.MongoClient("mongodb+srv://FinalDatabase:HyperHactive@cluster0.xdhqnvi.mongodb.net/FinalDatabase?retryWrites=true&w=majority")
db = client.FinalDatabase
collection = db.Final
requesting = []

# with open("C:\\Users\\srushti\\Desktop\\hyperhacktive\\data.json","r") as f:
#     for jsonObj in f:
#         print(jsonObj,type(jsonObj))
#         myDict = json.loads(jsonObj)
#         requesting.append(InsertOne(myDict))
# print(type(requesting))
# result = collection.bulk_write(requesting)
# client.close()

with open("C:\\Users\\srushti\\Desktop\\hyperhacktive\\data.json","r") as f:
    myDict = json.load(f)
    for jsonObj in myDict["student_detail"]:
        requesting.append(InsertOne(jsonObj))

result = collection.bulk_write(requesting)
client.close()

