from email import message
import bot, discord, misc, respond
from discord.ext import commands
#command prefix
pref = "-"
rm = respond.respondMap()

client = commands.Bot(command_prefix=pref)

@client.command()
async def addName(arg):
    print("it done happened")
    x = "test"
    rm.addResponse(str(x), str(arg))
    print(arg)

@client.event
async def on_connect():
    print("Connected to discord..")

@client.event
async def on_ready():
    print("Ready!")

@client.listen
async def on_message(message):
    resp = respond.findResponse(message)
    if(resp != ""):
        await message.channel.send(resp)

    if(message == "-mm"):
        await message.channel.send(rm)

#keep at end
client.run(misc.retKey())