import datetime
import sys
 
from django.template.loader import get_template
from django.template import Context
 
from django.http import HttpResponse
 
def test(request, data ):

    #http://192.168.1.118:8080/test/data   -- this is the format 
	print "temp is" + data 
	return HttpResponse("OK")
		

