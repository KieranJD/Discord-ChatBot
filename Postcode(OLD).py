import APIMaps as maps

'''Input:Object (message), Output: String (msg)'''
def Google(message):
		Postcode = str(message.content) # converting the discord message to a string
		Postcode = Postcode.replace("!GoogleMaps","")
		Postcode = Postcode.replace(" ","")
		Valid = True
		if Valid == False:
			msg = "That location doesn't exist!"
			return msg
		else:
			msg = maps.Results(Postcode)
			msg = "Here you go " + str(msg)
			return msg	

