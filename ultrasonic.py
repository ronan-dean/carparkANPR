from recognition.ultrasonicdriver import distance
from recognition.recognition_processing import ANPR
import time
import imutils
import cv2
def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

psm = 7
clearBorder = 1
debug = 0
anpr = ANPR(debug > 0)
dis = distance()
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_BRIGHTNESS,-25)
cam.set(cv2.CAP_PROP_GAMMA,-100)
def checkForCar():
    dis = distance()
    if dis <= 20:
        return(True)
def takePhoto():
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        return
    rotated = imutils.rotate_bound(frame, -180)
    image = imutils.resize(rotated, width=600)
    (lpText, lpCnt) = anpr.find_and_ocr(image, psm,
            clearBorder > 0)
        # only continue if the license plate was successfully OCR'd
    if lpText is not None and lpCnt is not None:
        # print the license plate to terminal 
        print(lpText)
        return lpText
if checkForCar() == True:
    print("Car found")
    takePhoto()


