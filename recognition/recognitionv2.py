import cv2
import time
import imutils
import numpy as np
import pytesseract
from PIL import Image
from skimage.segmentation import clear_border
cam = cv2.VideoCapture(0)
#cam.set(cv2.CAP_PROP_BRIGHTNESS,0)
#cam.set(cv2.CAP_PROP_GAMMA,0)
# This line takes a photo to iniatize the cam for faster processing on demand...
test1, imgX = cam.read() 
def ANPR(lang, debug):
	tic = time.perf_counter()
	ret, img = cam.read()
	img = imutils.resize(img, width=600)
	img = imutils.rotate_bound(img, -180)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
	gray = cv2.bilateralFilter(gray, 1, 1, 1) #Blur to reduce noise
	blur = cv2.GaussianBlur(gray,(5,5),0)
	edged = cv2.Canny(blur, 20, 120) #Perform Edge detection
	# find contours in the edged image, keep only the largest
	# ones, and initialize our screen contour
	cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
	screenCnt = 0
	# loop over our contours
	for c in cnts:
	# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.018 * peri, True)
	# if our approximated contour has four points, then
	# we can assume that we have found our screen
		if len(approx) == 4:
			screenCnt = approx
			break
		if screenCnt is 0:
			detected = 0
			print("No contour detected")
			return "none"
		else:
			detected = 1
	# Masking the part other than the number plate
	mask = np.zeros(gray.shape,np.uint8)
	new_image = cv2.drawContours(mask,[screenCnt],0,255,-5)
	new_image = cv2.bitwise_and(img,img,mask=mask)
	# Now crop
	(x, y) = np.where(mask == 255)
	(topx, topy) = (np.min(x), np.min(y))
	(bottomx, bottomy) = (np.max(x), np.max(y))
	Cropped = new_image[topx:bottomx+1, topy:bottomy+1]
	greyCropped = cv2.cvtColor(Cropped, cv2.COLOR_BGR2GRAY)
	rotated = imutils.rotate_bound(greyCropped, -1)
	roi = cv2.threshold(rotated, 0, 255,
		cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
	roi = clear_border(roi)
	if debug == 1:
		cv2.imshow("Image", gray)
		cv2.imshow("Edges", edged)
		cv2.imshow("ROI", roi)
		cv2.waitKey(0)
	#Read the number plate
	text = pytesseract.image_to_string(roi, config=f'--psm 7 -l {lang}')
	toc = time.perf_counter()
	print(f"time taken {toc - tic:0.4f}")
	return text