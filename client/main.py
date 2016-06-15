import time as t
from Relay import *
from Board import *
from Sensor import *
from HttpClient import * 
from threading import Thread

class MotionSensor(Sensor):
    def __init__(self, pin, httpclient):
		Sensor.__init__(self,pin)
		self.httpclient = httpclient
 
    def onStateChange(self,channel):
        print "%s: pin: %d state: %d" % (t.asctime(), channel, self.getState())
        if(self.getState()):
        	#send message to client
			self.httpclient.sendData("motion=1")


def boardSensorThread( relay,board, httpclient ,duration):	
	lightIsOn = False
	tempIsOn = False
	dataStr =None
	while True:
	
		light = board.light()
		temp = board.temperature()
		print "%s:  light:%d temp:%d " % (t.asctime(), light,temp)
		dataStr ="light=" + str(light)  
		if(board.light()<160):
			if(lightIsOn == False):
				print "on light relay"
				relay.switch(0,1)
				lightIsOn = True
				dataStr += "(on)"	
				
		else:
			if(lightIsOn == True):
				print "off light relay"
				relay.switch(0,0)
				lightIsOn = False
				dataStr += "(off)"	
				
		dataStr += ",temperature=" + str(temp)
		
			
		if(board.temperature()<100):
			if(tempIsOn == False):
				print "on temp relay"
				relay.switch(1,1)
				tempIsOn = True
				dataStr += "(on)"
		
				
		else:
			if(tempIsOn == True):
				print "off temp relay"
				relay.switch(1,0)
				tempIsOn = False
				dataStr += "(off)"
				
		
			
		httpclient.sendData(dataStr)
		
		t.sleep(duration)
	
   
def main():	
    #init client
    url = 'http://192.168.1.118:8080/'
    client = HttpClient(url)
    #init motionSensor
    motionSensor = MotionSensor(17, client)
    motionSensor.setEvent(GPIO.BOTH)
    #init relay
    relay = Relay()
    #init temperature sensor 
    board = Board()
    Thread(target=boardSensorThread, args=(relay,board,client,5)).start()

    while True:
        t.sleep(5)
 
if __name__ == "__main__":
    main()
