
import discord
import asyncio
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
prefix = "?"
TOKEN = 'NTY3MDg3NjY1ODEyNjAyODgw.XLObow.qMmmMxcU4UIcVZsXjHnFl_Yx5bw'
Client = commands.Bot(command_prefix=prefix)
client = discord.Client()
players= {}


@client.event
async def on_message(message):
    if message.content.startswith("?staff"):
        channel= client.get_channel("567314641424744479")
        msg = "!"+ "צריך עזרה"+" "+f"{message.author.mention}"+" " + "," + "<@&567322434911338516> <@&540590820085202974> <@&540590875881766912> <@&547499780176085003> ".format(message)
        msg2 = "`Waiting For Staff`"+" "+"בשביל לקבל עזרה המתן בחדר" .format(message)
        await client.send_message(channel,msg)
        await client.send_message(message.author,msg2)
    
                                 














@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Member Count:'))
    print('Logged in as')   
    print(client.user.name)
    print(client.user.id)
    print('------') 

client.run(TOKEN)
