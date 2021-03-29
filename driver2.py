import time
# Import driver for our ultrasonic
from drivers.ultrasonicdriver import distance
# Import driver for our ~new~ Plate recognition
from drivers.recognitionv2 import ANPR
# Database set up
import pymongo
import os
password = os.environ['MONGOPWD']
myclient = pymongo.MongoClient(f"mongodb+srv://ronanR:{password}@cluster0.fjaqs.mongodb.net/carpark?retryWrites=true&w=majority")
mydb = myclient["carpark"]
mycol = mydb["v0.1.1"]
from datetime import datetime
from datetime import timedelta

userCommand = input("1. Enter 2. Exit 3. Search ")
if userCommand == '1':
    dis = distance()
    while dis >= 23:
        print("waiting for the car")
        dis = distance()
        if dis <= 22:
            text = ANPR()
            user = {"plate": text, "timeEntered": datetime.now(), "exited": False}
            mycol.insert_one(user)
            print("Plate entered")
if userCommand == '2':
    dis = distance()
    while dis >= 23:
        print("Waiting for car to arrive")
        dis = distance()
        if dis <= 22:
            text = ANPR()
            query = {"plate": text}
            mycol.update_many(query, {"$set": { "exited": True, "timeExited": datetime.now()}})
            print("car exited")
if userCommand == '3':
    text = ANPR()
    query = { "plate": text }
    result = mycol.find(query,{"_id": 0 })
    for x in result:
        print(x)