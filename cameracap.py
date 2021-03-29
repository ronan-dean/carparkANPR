import cv2
import imutils
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_BRIGHTNESS,0)
cam.set(cv2.CAP_PROP_GAMMA,-100)
cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    # rotate the image becuase its upside down
    image = imutils.resize(frame, width=600)
    rotated = imutils.rotate_bound(image, -180)
    cropped = rotated[190:180, 200:300]
    cv2.imshow("test", rotated)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, cropped)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()
