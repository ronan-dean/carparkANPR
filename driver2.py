# Import ANPR script
from recognition.recognitionv2 import ANPR
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

print("calling anpr")
text = ANPR()
print("ANPR done")
print(text)
if text == "none":
    text = ANPR()
    print(text)
