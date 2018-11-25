import discord
from flask import Flask, jsonify
import requests
from Key import Weather_key


'''Function: Requests the Weather Dictionary from the Open Weather API via Latitude and Longitude.
Input: Float(Lat,Lng), Output: Dictionary(Search_json)'''
def Forecast(Lat,Lng):
	Lat = str(Lat)
	Lng = str(Lng)
	Weather_Api = "http://api.openweathermap.org/data/2.5/weather?lat="+(Lat)+"&lon="+(Lng) # The Open Weather api Url.
	Search_Input = { "APPID":Weather_key,}
	Search_Req = requests.get(Weather_Api,Search_Input) # Requests the specific dictionary from the Open Weather API
	Search_Json = Search_Req.json() # Json representaion of dictionary returned. 
	print("\n",Search_Json)
	return(Search_Json) # Returns to APIMaps.py


