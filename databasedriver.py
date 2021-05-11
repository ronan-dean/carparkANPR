import pymongo
from datetime import datetime
from datetime import timedelta
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["carpark"]

mycol = mydb["paymenttesting"]
action = input("1. Find Time 2. Enter car 3. Exit car")
if action == "1":
    find = input("Enter car plate: ")
    query = { "plate": find }
    result = mycol.find(query,{"_id": 0 })
    for x in result:
        print(x)
if action == "2":
    plate = input("Car plate: ")
    user = {"plate": plate, "timeEntered": datetime.now(), "exited": False}
    mycol.insert_one(user)
    print("car entered")
if action == "3":
    exit = input("Car plate to exit: ")
    query = {"plate": exit}
    mycol.update_many(query, {"$set": { "exited": True, "timeExited": datetime.now()}})
    print("car exited")