# Seat Geek API 

import time
from pprint import pprint
from SeatGeekFunctions import *


def main():
	#main code


	for show in fncGetConcerts():
		#pprint(show)
		# Get updated SeatGeek Data 
		#print(show['concert_id'])
		id = show['concert_id']
		title = show['title']
		data = fncGetSeatGeekData(id)
		print(title + " - " + data['datetime_local'])
		#Check 'old' lowest price vs 'new' lowest price
		fncCheckValues(id,show['lowest_price'],data['stats']['lowest_price'], 'lowest_price', title)
		fncCheckValues(id,show['ticket_count'],data['stats']['listing_count'], 'ticket_count', title)
		fncCheckValues(id,show['average_price'],data['stats']['average_price'], 'average_price', title)
		

		fncLastChecked(id)

		# Log Hiostory
		#fncWriteLog(id,data)

####################################
####################################
####################################
if __name__ == "__main__":
	#while True:
	#	print("Running Now ", printTimestamp())
	#	main()
	#	time.sleep(10)
	main()