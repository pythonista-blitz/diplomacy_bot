# モジュールインポート
import discord
import json
from collections import OrderedDict
import pprint

f = open('../config/config.json', 'r')
load_config = json.load(f)
pprint.pprint(f)
BOT_ACCESS_TOKEN = load_config["TOKEN"]

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
    elif message.content == '/nekoparadise':
        await message.channel.send('にゃーんにゃーんにゃーんにゃーんにゃーんにゃーんにゃーんにゃーんにゃーん')
    elif message.content == '/mk3':
        await message.channel.send('mk3はい')

client.run(BOT_ACCESS_TOKEN)
