import time as t
from Relay import *
from Board import *
from Sensor import *
from threading import Thread

class MotionSensor(Sensor):
    def __init__(self, pin):
        Sensor.__init__(self,pin)
 
    def onStateChange(self, channel):
        print "%s: pin: %d state: %d" % (t.asctime(), channel, self.getState())
        #if(self.getState())
        	#send message to client 


def boardSensorThread( board, duration):	
    while True:
        print "%s: control:%d light:%d temp:%d custom:%d" % (t.asctime(),
                               board.control(),
                               board.light(),
                               board.temperature(),
                               board.custom())
        t.sleep(duration)
   
def main():	
	
	#init motionSensor
    motionSensor = MotionSensor(17)
    motionSensor.setEvent(GPIO.BOTH)
    #init relay
    relay = Relay()
    #init temperature sensor 
    board = Board()
    Thread(target=boardSensorThread, args=(board, 3)).start()

    while True:
        t.sleep(1)
 
if __name__ == "__main__":
    main()