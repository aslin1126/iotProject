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


def boardSensorThread( relay,board, duration):	
	lightIsOn = False
	tempIsOn = False
	while True:
		print "%s:  light:%d temp:%d " % (t.asctime(), board.light(),board.temperature())
		if(board.light()<160):
			if(lightIsOn == False):
				print "on light relay"
				relay.switch(0,1)
				lightIsOn = True
		else:
			if(lightIsOn == True):
				print "off light relay"
				relay.switch(0,0)
				lightIsOn = False

		if(board.temperature()<100):
			if(tempIsOn == False):
				if(tempIsOn == False):
					print "on temp relay"
					relay.switch(1,1)
					tempIsOn = True
		else:
			if(tempIsOn == True):
				print "off temp relay"
				relay.switch(1,0)
				tempIsOn = False

		t.sleep(duration)
	
   
def main():	
	
	#init motionSensor
    motionSensor = MotionSensor(17)
    motionSensor.setEvent(GPIO.BOTH)
    #init relay
    relay = Relay()
    #init temperature sensor 
    board = Board()
    Thread(target=boardSensorThread, args=(relay,board,3)).start()

    while True:
        t.sleep(5)
 
if __name__ == "__main__":
    main()