import discord 
import requests
from datetime import datetime

client = discord.Client()

TOKEN = "ODcwMDU5NTM4NDk2MjI5NDE3.YQHQFg.99-Z31piEWQu8hLId2egjCVeblU"
TOKEN_IVAN = "Nzk2NTQ0ODI5ODM2MjMwNjg2.X_ZeLg.2PJJ_aIkSdrVGxproLUriZtgPeA"

# Function to call hypixel API to get the data
def getHypixelData():

    PARAMS = {"key": "62829fb1-9764-4f32-bc02-baa7f6c46637",  "name": "enderdrxgon"}
    r  = requests.get( url = "https://api.hypixel.net/player", params = PARAMS)
    return r.json()

@client.event
async def achievements(message):
 
    data = getHypixelData()

    player_achievements = data["player"]["achievementPoints"]
    
    result = "enderdrxgon's achievement points: "   + str(player_achievements) 
    await message.channel.send( result )
    return

@client.event 
async def on_ready():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Bot is online " + current_time)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-ap'):
        await achievements(message)

### Entry point to start the client
client.run(TOKEN_IVAN)
