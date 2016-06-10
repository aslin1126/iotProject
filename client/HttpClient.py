import urllib
import urllib2

class HttpClient:
	def __init__(self, url):
		self.url = url

	def sendBoardData(self, temp, light ):
		print temp + "," + light
		getUrl =  self.url + "test/"
		if(temp!= None and light != None ):
			getUrl += "tempature="+ temp + ",light="+light	
			
		if(light != None  and temp == None ):
			getUrl += "light="+light
			
		if(light == None  and temp != None):
			getUrl += "tempature="+ temp
			
		print "send board infomation" + getUrl
		f = urllib2.urlopen(getUrl)
		f.close()
		
	def sendMotionAlert(self, status):
		getUrl = self.url + "test/motion='"+ status +"'"
		print "send motion alert"
		f = urllib2.urlopen(getUrl)
		f.close()


