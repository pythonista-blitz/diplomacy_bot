# モジュールインポート
import discord
import json
from collections import OrderedDict
import pprint

f = open('config.json')
config = json.load(f)
print(f)
BOT_ACCESS_TOKEN = f["TOKEN"]

client = discord.Client()

@client.event
async def on_ready():
    print('Login Successful')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    elif message.content == '/mk3':
        await message.channel.send('mk3はい')

client.run(BOT_ACCESS_TOKEN)
