import pymongo
from datetime import datetime
from datetime import timedelta
# car park pymongoset up
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["carpark"]
mycol = mydb["paymenttesting"]
# card payment pymongo set up 
paydb = myclient["carpark"]
paycol = paydb["cardtesting"]

mycard = "1234"
myplate = "abc-def"
query = { "card": mycard }
cursor = mycol.find(query)

count = mycol.count_documents({"plate": myplate})
if count == 1:
    print("This is a new car")
if count == 0:
    print("Bad reading from plate")
if count > 1:
    print("searching for non exited stamp")
    carCount = mycol.count_documents({"plate": myplate, "exited": False})
    if carCount == 1:
        print("Found an unexited car")
        carResult = mycol.find_one({"plate": myplate, "exited": False})
        print(carResult["time"])
        card = carResult["card"]
        payCard = paycol.find_one({"card": card})
        print(payCard)
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

        
        

    
