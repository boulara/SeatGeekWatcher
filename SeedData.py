
import http.client, urllib
import requests, json
import pymongo
import datetime
from pymongo import MongoClient



# Connect to ConcertsDB
client = MongoClient()
db = client.concerts

### Delete all Data
db.concerts.drop()

#Check if empty
print(db.concerts.count(), " Records Found")
x = {
	"title" : "Kenny Chesney with Chase Rice",
	"concert_id" : "2425740",
	"concert_url" : "https://seatgeek.com/kenny-chesney-with-chase-rice-tickets/uncasville-connecticut-mohegan-sun-arena-2015-04-25-7-30-pm/concert/2425740/",
	"last_checked" : "2014-12-13T15:42:12.733075",
	"concert_date" : "2015-04-25T23:30:00",
	"ticket_count" : 0,
	"ticket_count_trend" : "None",
	"lowest_price" : 0,
	"lowest_price_trend" : "None",
	"average_price" : 0,
	"average_price_trend" : "None"
}



### Load New Data

db.concerts.insert(x)


#Check for records again
print(db.concerts.count(), " Records Found")