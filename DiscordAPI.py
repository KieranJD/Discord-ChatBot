import discord
import Location as location

TOKEN = 'NTAyMjI2MDYzNzYyMzkxMDUw.Dqk38g.KFDtyaHwMfRNK6RRUKYfpDj9L9Y' # The Discord Bot's token.

client = discord.Client()

'''Function: Takes the "message" object from the Discord channel and interprets it. 
Input: Object(message), Output: String(msg,Advice,content[0]),Embed(embed) '''
@client.event
async def Server(message):
	if message.author == client.user: # To prevent the bot from replying to itself.
		return
	msg = ""
	if message.content.startswith('!GoogleMaps'):
		Run = "Maps"
		msg = msg + str(location.Google(message,Run)) # Calls function "Google" from GoogleMaps.py
		await client.send_message(message.channel,msg)
	elif message.content.startswith('!Timezone'):
		Run = "Time"
		msg = msg + str(location.Google(message,Run))
		await client.send_message(message.channel, msg)
	elif message.content.startswith('!Weather'):
		Run = "Weather"
		Content = location.Google(message,Run)
		Advice = str(Content[2]) +"\n" + str(Content[3]) # Concatenates the Temp and Condition varibles that are returned. 	
		embed = discord.Embed() # This allows for the icon image to be inputted into discord.
		embed.set_image(url=Content[1]) # Sets the embed image to the url of the  Icon_Url variable returned.
		while True:
			try:
				await client.send_message(message.channel,Content[0],embed=embed) # Sends the msg variable that is returned (current weather) and the icon.
				await client.send_message(message.channel,Advice) # Sends the Advice string to the channel.
				break		
			except: # If the place doesn't exist.
				msg = "That location doesn't exist or it is not specific enough!"
				await client.send_message(message.channel,msg)
				break
	elif not msg: # To prevent an empty message being sent
		return
	
'''Function: Detects an input message in the discord channel and then sends the arugument to the "Server" function.
Input: Object(message), Output: Object(message)'''
@client.event
async def on_message(message): # Must be called "on_message", detects a message in Discord.
	print(message.content)
	await Server(message) # "await" to allow print("message.content") to be executed.

'''Function prints to console to show program is running'''
@client.event
async def on_ready(): # Must be called "on_ready" 
	print('Logged in as ' + client.user.name)

client.run(TOKEN) # To run the Discord Bot


