import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio_trigger = 18
gpio_echo = 24
gpio.setup(gpio_trigger, gpio.OUT)
gpio.setup(gpio_echo, gpio.IN)
def distance(): 
    gpio.output(gpio_trigger, True)
    time.sleep(0.0001)
    gpio.output(gpio_trigger, False)
    StartTime = time.time()
    StopTime = time.time()
    while gpio.input(gpio_echo) == 0:
        StartTime = time.time()
        
    while gpio.input(gpio_echo) == 1:
        StopTime = time.time()
    
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance