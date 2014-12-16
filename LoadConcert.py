
import http.client, urllib
import requests, json
import pymongo
import sys
import datetime
from pymongo import MongoClient
from SeatGeekFunctions import *
from pprint import *



ShowID = sys.argv[1]

if (ShowID is None):
	Print('Error:')


# Connect to ConcertsDB
client = MongoClient()
db = client.concerts

data = fncGetSeatGeekData(ShowID)

pprint(data)
x = {
	"title" : data['title'],
	"concert_id" : ShowID,
	"concert_url" : data['url'],
	"img_link": data['performers'][0]['images']['medium'],
	"last_checked" : "2014-12-13T15:42:12.733075",
	"concert_date" : "2015-04-25T23:30:00",
	"ticket_count" : 0,
	"ticket_count_trend" : "None",
	"lowest_price" : 0,
	"lowest_price_trend" : "None",
	"average_price" : 0,
	"average_price_trend" : "None"
}

print(x)

### Load New Data

db.concerts.insert(x)


#Check for records again
print(db.concerts.count(), " Records Found")