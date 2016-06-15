import urllib
import urllib2

class HttpClient:
	def __init__(self, url):
		self.url = url

	def sendData(self, data):
		print data 
		getUrl = self.url + "saverecord/"+ data
		f = urllib2.urlopen(getUrl)
		f.close()



