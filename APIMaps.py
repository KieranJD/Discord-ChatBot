from flask import jsonify
import requests
from Key import key
import TimeZone as timez
import Weather as weather

Search_Api = "https://maps.googleapis.com/maps/api/place/textsearch/json"
Details_Api ="https://maps.googleapis.com/maps/api/place/details/json"


"""Function: Does Request operations to return specific values from the Google Places API.
Input: String(Location,Run), Output: String(url,timez.Tzone(Lat,Lng)) Dictionary:(weather.Forecast(Lat,Lng)),"""
def Results(Location,Run):
	Search_Input = {"key":key, "query":Location} # My API key and the location.
	Search_Req = requests.get(Search_Api,Search_Input) # Requests the Search dictionary with my key and the api url.
	Search_Json = Search_Req.json() # Json representaion of dictionary returned.
	print(Search_Json) 
	if Run == "Maps":
		Place_Id = Search_Json["results"][0]["place_id"] # Sets "Place_Id" to be the value of "place_id" key in the specific api dictionary requested.
		Details_Input = {"key":key, "placeid":Place_Id}
		Details_Req = requests.get(Details_Api,Details_Input) # Requests the Deatils dictionary.
		Details_Json = Details_Req.json()
		Url = Details_Json["result"]["url"] # Sets "URl" to be the value of "url" key in the specific details api dictionary requested.
		return Url # Returns to Location.py
	else:
		Lat = Search_Json["results"][0]["geometry"]["location"]["lat"]
		Lng = Search_Json["results"][0]["geometry"]["location"]["lng"]
		if Run == "Time":
			return(timez.Tzone(Lat,Lng)) # Returns to Location.py
		else:
			return(weather.Forecast(Lat,Lng)) # Returns to Location.py

"""Function: Takes the user's "location" input and and sets "Addresss" to be the formal format of the location requested from the API dictionary.
Input: String(Location), Output: String(Address)"""
def Format_Adr(Location):
	Search_Input = {"key":key, "query":Location}
	Search_Req = requests.get(Search_Api,Search_Input) 
	Search_Json = Search_Req.json() 
	Address = Search_Json["results"][0]["formatted_address"]
	return Address
	

