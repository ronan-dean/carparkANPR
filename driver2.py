# Import ANPR script
from recognition.recognitionv2 import ANPR
from recognition.rfiddriver import readTag
from imutils import paths
import argparse
import imutils
import cv2
import time
# Add database supports
import pymongo
from datetime import datetime
from datetime import timedelta
# Configure database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["carpark"]
mycol = mydb["v0.2"]

a = 10 
errorCount = 0
for x in range(a):
    plate = ANPR("straightplate", 0)
    print(plate)
    if plate == "none":
        errorCount = errorCount + 1
sucessRate = 10 - errorCount
sucessRate = sucessRate * 10
print(f"{sucessRate}%")


    