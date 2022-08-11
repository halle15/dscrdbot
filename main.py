from email import message
import bot, discord, misc, respondMap
from discord.ext import commands
#command prefix
pref = "-"
rm = respondMap.respondMap()

client = commands.Bot(command_prefix=pref)

@client.command()
async def addName(ctx, arg):
    

    x = "test"
    response = rm.addResponse(str(x), str(arg))
    print(response)
    if response:
        await ctx.channel.send(response)
    else:
        await ctx.channel.send("You don't know what you're doing!")
    print(arg)

@client.event
async def on_connect():
    print("Connected to discord..")

@client.event
async def on_ready():
    print("Ready!")

@client.listen()
async def on_message(message):
    resp = rm.findResp(message)
    print(resp)
    if(resp != ""):
        await message.channel.send(resp)

    if(message == "-mm"):
        await message.channel.send(rm)

#keep at end
client.run(misc.retKey())