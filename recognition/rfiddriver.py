from pirc522 import RFID
rdr = RFID()
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def readTag():
  rdr.wait_for_tag()
  (error, tag_type) = rdr.request()
  if not error:
    print("Tag detected")
    (error, uid) = rdr.anticoll()
    if not error:
      print("read")
  rdr.cleanup()
  return uid