import pymongo
from datetime import datetime
from datetime import timedelta
myclient = pymongo.MongoClient("mongodb+srv://ronanpi:Nuggets1@cluster0.fjaqs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydb = myclient["carpark"]
mycol = mydb["paymenttesting"]
paycol = mydb["cardtesting"]

def enterCar(plate):
    user = {"plate": plate, "timeEntered": datetime.now(), "exited": False}
    mycol.insert_one(user)
    print(f"{plate} entered")

def exitCar(plate, card):
    carResult = mycol.find_one({"plate": plate, "exited": False})
    print(card)
    payCard = paycol.find_one({"card": card})
    print(payCard)
    timeInPark = datetime.now() - carResult["timeEntered"]
    print("This car spent", timeInPark, "time in the car park")
    mins = timeInPark.total_seconds() / 60
    print("Total time in mins", mins)
    mycol.update_one({"_id": carResult["_id"]}, {"$set": {"exited": True}})
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
   


