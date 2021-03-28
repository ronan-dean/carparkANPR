from recognition.recognition_processing import ANPR
from imutils import paths
import argparse
import imutils
import cv2
def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

imagePaths = sorted(list(paths.list_images("photos")))
psm = 7
clearBorder = 1
debug = 0
anpr = ANPR(debug > 0)
print(debug)
for imagePath in imagePaths:
	# load the input image from disk and resize it
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=600)
	# apply automatic license plate recognition
	(lpText, lpCnt) = anpr.find_and_ocr(image, psm,
		clearBorder > 0)
	# only continue if the license plate was successfully OCR'd
	if lpText is not None and lpCnt is not None:
	   
		# show the output ANPR image
	    print("[INFO] {}".format(lpText))
