import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN)
import time

while GPIO.input(37) == 0:
    print("Car is above")
    time.sleep(0.5)
while GPIO.input(37) == 1:
    print("No car yet")
    time.sleep(0.5)
time.sleep(0.5)