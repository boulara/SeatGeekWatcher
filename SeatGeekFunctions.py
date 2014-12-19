
import http.client, urllib
import requests, json
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient()
db = client.concerts

def fncGetConcerts():
	return db.concerts.find()

def updateDbQty(id,qty):
    db.concerts.update({'concert_id': id}, {'$set': {'ticket_count': qty}})

def printTimestamp():
    return datetime.datetime.now().isoformat()

def fncTrend(old,new):
    if old < new:
        return "Higher"
    else:
        return "Lower"

def fncGetSeatGeekData(concert_id):
    url = 'http://api.seatgeek.com/2/events/'+ str(concert_id)
    print(url)
    r = requests.get(url)
    if (r.status_code == 200):
        return r.json()
    else:
        print('Error', r.status_code)
        text = "Error: " + r.status_code
        fncSendPushover(text)

def fncCheckValues(id,old,new,parm, title):
	#print('#######',old['lowest_price'])
	#print(old, ' ### ', new)
	trendName = parm + '_trend'
	if (new > old):
		db.concerts.update({'concert_id': id}, {'$set': {parm: new, trendName: fncTrend(old,new)}})
		text = title + " " + parm + " Changed ", new
		fncSendPushover(text)
		print('DB Updated >> ', parm)
	else:
		print("No DB Updates >> ", parm)


def fncLastChecked(id):
	db.concerts.update({'concert_id': id}, {'$set': {'last_checked': printTimestamp()}})


def fncSendPushover(alert):
	conn = http.client.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
  	urllib.parse.urlencode({
    	"token": "aP4DDU14mE6rPQrrLTcxxBWWRDkVGM",
    	"user": "uHEMkqk8JcqYkTg7UktHPusRqf5UtF",
    	"message": alert,
 	}), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()

def fncWriteLog(id,data):
	db.concerts.update({'concert_id': id}, {'$set' : {'history': { printTimestamp(): {'ticket_count': data['stats']['listing_count']}}}})
