import datetime
import sqlite3
import sys
import re

from django.template.loader import get_template
from django.template import Context

from django.http import HttpResponse

def home(request):
    dt = datetime.datetime.now()
    html = '''
<html><body><h1>From django</h1>
<p>Time now: %s.
</body></html>''' % (dt,)
    return HttpResponse(html)

def listrecords(request):
    connection = None
    data = dict()
    data['title'] = "List of records"
    try:
        connection = sqlite3.connect('/home/pi/iotProject/iotserver/db.sqlite3')
        with connection:
            cursor1 = connection.cursor()
            cursor1.execute("select * from record order by 1 desc limit 1")
            data['records1'] = cursor1.fetchall()

            cursor2 = connection.cursor()
            cursor2.execute("select * from record order by 1 desc limit 10")
            data['records2'] = cursor2.fetchall()
            print  data['records1'][0]
            print  data['records2'][0]
            data['records2'].pop(0)
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if connection:
            connection.close()
    html = get_template('listrecords.html').render(Context(data))
    return HttpResponse(html)

def saverecord(request,data):
    #http://192.168.1.118:8080/views/data   -- this is the format 
    print "new data is " + data    
    
    connection = None
    try:
        connection = sqlite3.connect('/home/pi/iotProject/iotserver/db.sqlite3')
        with connection:
            cursor = connection.cursor()    
            cursor.execute("INSERT INTO record VALUES (?)", [data])
    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if connection:
            connection.close()
    return HttpResponse("New data '"+data+"' is saved")
