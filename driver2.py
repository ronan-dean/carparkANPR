# Import ANPR script
from recognition.recognitionv2 import ANPR
from recognition.rfiddriver import readTag
from recognition.databasedriver import enterCar
from recognition.databasedriver import exitCar
from imutils import paths
import argparse
import imutils
import cv2
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN)
# Add database supports
import pymongo
from datetime import datetime
from datetime import timedelta
# Configure database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["carpark"]
mycol = mydb["v0.2"]
action = input("1. enter carpark 2. exit carpark: ")
if action == str("1"):
    GPIO.wait_for_edge(37,GPIO.FALLING)
    GPIO.remove_event_detect(37)
    plate = ANPR("straightplate", 0)
    print(plate)
    enterCar(plate)
if action == str("2"):
    GPIO.wait_for_edge(37,GPIO.FALLING)
    GPIO.remove_event_detect(37)
    plate = ANPR("straightplate", 0)
    print(plate)
    print("Waiting to read tag")
    uid = readTag()
    uid = str(uid)
    print(uid)
    exitCar(plate, uid)


    