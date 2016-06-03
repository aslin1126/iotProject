import urllib
import urllib2
import sys
url = 'http://192.168.1.118:8080/'
values = { 'var': 'test' }

try:
    data = urllib.urlencode(values, doseq=True)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print response.readline()
except:
    the_page = sys.exc_info()
    raise