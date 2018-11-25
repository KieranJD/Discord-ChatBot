from flask import jsonify
import requests
from Key import key
import time
import datetime

Time_Api = "https://maps.googleapis.com/maps/api/timezone/json?"

"""Function: Requests the locations Timezone dictionary via Longitude and Latitude to then be manipulated.
Input: integer(Lat,Lng), Output: String(Newtime,Time_Zone,Time_Name)"""
def Tzone(Lat,Lng):
	Timestamp = time.time() # Seconds since epoch 1st Jan 1970.
	Search_Input = {'location': "%s,%s" % (Lat, Lng), "timestamp":Timestamp,"key":key,} # My API key, Timestamp and the location in longitude and latitude.
	Search_Req = requests.get(Time_Api,Search_Input) # Requests the dictionary for specific location using my key and the Search_Input.
	Search_Json = Search_Req.json() # Json representaion of dictionary returned. 
	print("\n",Search_Json)
	Time_Zone = Search_Json["timeZoneId"] # Sets "Time_Zone" to be the value of "timeZoneId" key in the specific api dictionary requested.
	Time_Name = Search_Json["timeZoneName"]
	Time_Time = int(Search_Json["rawOffset"]/3600) # Fetches hourOffset and divides by 3600 to get it in hours.
	Time_Daylight = int(Search_Json["dstOffset"]/3600) # Fetches Daylight saving configuration and divides by 3600 to get it in hours.
	Newtime = Clock(Time_Time,Time_Daylight)
	return(Newtime,Time_Zone,Time_Name) # Returns to APIMaps.py

'''Function: Adjusts the current clock time to the correct time for the Timezone.  
Input:Integer (Time_Time,Time_Daylight), Output: String(Newtime)'''
def Clock(Time_Time,Time_Daylight): # Adjusting time
	Now = datetime.datetime.now() # Sets "Now" to the current time. 
	Hour = Now.hour + Time_Time + Time_Daylight  
	if Hour>23: # Timezones infront  
		Hour = Hour - 24
	if Hour+Time_Time<0: # Timezones behind
		Hour = Hour + 24
	Newtime = datetime.time(Hour, Now.minute, Now.second) # Sets "Nettime" to the correct time for the location.
	Newtime = str(Newtime)
	return(Newtime) # Returns to APIMaps.py
	
	
	
	
