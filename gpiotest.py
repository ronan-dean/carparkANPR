import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
import time

while GPIO.input(17) == 0:
    print("Car is above")
    time.sleep(0.5)
while GPIO.input(17) == 1:
    print("No car yet")
    time.sleep(0.5)
time.sleep(0.5)