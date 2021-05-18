import pymongo
from datetime import datetime
from datetime import timedelta
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["carpark"]
mycol = mydb["paymenttesting"]

def enterCar(plate):
    user = {"plate": plate, "timeEntered": datetime.now(), "exited": False}
    mycol.insert_one(user)
    print(f"{plate} entered")

def exitCar(plate, card):
    carResult = mycol.find_one({"plate": plate, "exited": False})
    payCard = paycol.find_one({"card": card})
    timeInPark = datetime.now() - carResult["time"]
    print("This car spent", timeInPark, "time in the car park")
    mins = timeInPark.total_seconds() / 60
    print("Total time in mins", mins)
    if mins <= 60:
        print("cost is $2")
        u = payCard["lastBal"] - 2
        paycol.update_one({"card": payCard["card"]}, {"$set": {"balance": u}})
    if mins > 60 and mins < 119:
        print("cost is $4")
        u = payCard["lastBal"] - 4
        print("updating database now")
        paycol.update_one({"card": payCard["card"]}, {"$set": {"balance": u}})
    if mins > 120 and mins < 179:
        print("cost is $6")
        u = payCard["lastBal"] - 6
        print("updating database now")
        paycol.update_one({"card": payCard["card"]}, {"$set": {"balance": u}})
    if mins > 180:
        print("cost is $10")
        u = payCard["lastBal"] - 10
        print("updating database now")
        paycol.update_one({"card": payCard["card"]}, {"$set": {"balance": u}})
    mycol.update_many(query, {"$set": { "exited": True, "timeExited": datetime.now()}})
    print(f"{plate} exited")

