import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
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
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured distance = %.1f cm" % dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped y user")
        gpio.cleanup()