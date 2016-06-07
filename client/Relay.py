import RPi.GPIO as GPIO
import sys
 
class Relay:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.pinList = [22,23,24,25]
 
    def switch(self, lamp, state):
        print "switch"
        pin = self.pinList[lamp]
        print "switch and pin is " + str(pin) 
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, (GPIO.HIGH if state == 0 else GPIO.LOW))