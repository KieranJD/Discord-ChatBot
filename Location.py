import APIMaps as maps
from PIL import Image
import requests

'''Function: Extracts the location from the User's "message" input and also creates the msg to be sent to the Discord channel.
Input: Object(message),String(Run), Output: String(msg,Icon_url,Temp,Condition)'''
def Google(message,Run):
		while True:
			try:
				Location = str(message.content) # Converting the discord message to a string so it can be modified.
				Location = Location.replace("!GoogleMaps","")
				Location = Location.replace("!Timezone","")
				Location = Location.replace("!Weather","")
				Location = Location.lstrip(' ') # Removes and white spacing on the left.
				Location = Location.title()
				Content = maps.Results(Location,Run) # Calls the Results function in APIMaps.py to get specific data, example Url or Weather dictionary.
				if Run == "Maps":
					msg = "Here you go " + str(Content) # Concatenates "Here you go" with the string Url.
					return msg # Returns to Discord.py
				elif Run == "Time":
					msg = "The current time in " + maps.Format_Adr(Location) + " is "+ str(Content[0]) + " " + str(Content[2]) + " taken from " + str(Content[1]) # Content[0] is the time, Content[1] is the timezone and Content[2] is the city it's referencing.
					return msg # Returns to Discord.py
				else:
					Icon = Content['weather'][0]['icon']
					Icon_Url = "http://openweathermap.org/img/w/"+str(Icon)+".png" # Creates the specific icon Url.
					msg = "The current weather in " + maps.Format_Adr(Location) + " is " + str(Content['weather'][0]['description'])
					Celsius = round((Content['main']['temp'])- 273.15,1) # Coverting Kelvin to Celsius
					Temp = "The temperature is " + str(Celsius) + "ºC"
					if Content['weather'][0]['main'] == "Rain" or Content['weather'][0]['main'] == 'Thunderstorm':
						Rain = True
					else:
						Rain = False
					Condition = Advice(Celsius,Rain)
					return(msg,Icon_Url,Temp,Condition) # Returns to DiscordAPI.py
			except IndexError: # When the location is not in the api dictionary.
				msg = "That location doesn't exist or it is not specific enough!"
				return msg # Returns to Discord.py

"""Fucntion: Creates a "Condition" string which depends on what value Temp is and if Rain is True or Flase.
Input: Boolean(Rain),Float(Celcsius), Output: (Condition)"""
def Advice(Celsius,Rain):
	if -20 < Celsius < 0:
		Condition = "It's FREEZING! Make sure to wrap up warm if you plan to go outside there!"
	elif Celsius < -19:
		Condition = "It's beyond FREEZING! Only go outside if it's necessary and make sure to wear very insulating clothes."
	elif 0 < Celsius < 16:
		Condition = "It's CHILLY out there! Make sure put a jumper on!"
		if Rain == True:
			Condition = Condition + " "+ "Also don't forget your coat!"
	elif 16 < Celsius < 21:
		Condition = "It's warm out there, but not quite shorts weather!"
		if Rain == True:
			Condition = Condition + " " + "Also don't forget your coat!"
	elif 20 < Celsius < 31:
		Condition = "It's nice and warm! Have fun but make sure to put suncream on if you burn easily."
		if Rain == True:
			Condition =  "It's nice and warm! However, it's raining so don't forget your coat!"
	elif 30 < Celsius < 51:
		Condition = "It's very HOT out there! Perfect holiday weather! Make sure to use suncream and drink plenty of water!"
		if Rain == True:
			Condition =  "It's very HOT out there! However, it's raining so not beach weather, also don't forget your coat!"
	elif Celsius > 50:
		Condition = "It's RIDICULOUSLY HOT! Don't go outside unless necessary!" 
	return Condition	
