# Import ANPR script
from recognition.recognition_processing import ANPR
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
mycol = mydb["v0.1.1"]
def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()
imagePaths = sorted(list(paths.list_images("photos")))
psm = 7
clearBorder = 1
debug = 0
anpr = ANPR(debug > 0)
test1 = input("1. Enter 2. Exit 3. Search ")
if test1 == "1":
    tic = time.perf_counter()
    for imagePath in imagePaths:
        # load the input image from disk and resize it
        image = cv2.imread(imagePath)
        image = imutils.resize(image, width=600)
        # call the apnr class and apply to images
        (lpText, lpCnt) = anpr.find_and_ocr(image, psm,
            clearBorder > 0)
        # only continue if the license plate was successfully OCR'd
        if lpText is not None and lpCnt is not None:
            # print the license plate to terminal 
            print("[INFO] {}".format(lpText))
            user = {"plate": lpText, "timeEntered": datetime.now(), "exited": False}
            mycol.insert_one(user)
            print("Plate entered")
    toc = time.perf_counter()
    print(f"time taken {toc - tic:0.4f}")
if test1 =="2":
    tic = time.perf_counter()
    for imagePath in imagePaths:
        # load the input image from disk and resize it
        image = cv2.imread(imagePath)
        image = imutils.resize(image, width=600)
        # call the apnr class and apply to images
        (lpText, lpCnt) = anpr.find_and_ocr(image, psm,
            clearBorder > 0)
        # only continue if the license plate was successfully OCR'd
        if lpText is not None and lpCnt is not None:
            # print the license plate to terminal 
            print("[INFO] {}".format(lpText))
            query = {"plate": lpText}
            mycol.update_many(query, {"$set": { "exited": True, "timeExited": datetime.now()}})
            print("car exited")
    toc = time.perf_counter()
    print(f"time taken {toc - tic:0.4f}")
if test1 == "3":
    for imagePath in imagePaths:
        # load the input image from disk and resize it
        image = cv2.imread(imagePath)
        image = imutils.resize(image, width=600)
        # call the apnr class and apply to images
        (lpText, lpCnt) = anpr.find_and_ocr(image, psm,
            clearBorder > 0)
        # only continue if the license plate was successfully OCR'd
        if lpText is not None and lpCnt is not None:
            # print the license plate to terminal 
            print("[INFO] {}".format(lpText))
            query = { "plate": lpText }
            result = mycol.find(query,{"_id": 0 })
            for x in result:
                print(x)
else:
    print("waiting")
