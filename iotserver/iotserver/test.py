import datetime
import sys
 
from django.template.loader import get_template
from django.template import Context
 
from django.http import HttpResponse
 
def test(request):

	if request.method == 'GET':
		return HttpResponse("<p> this is get </p>")
	else:
		return HttpResponse("this is post")
 
