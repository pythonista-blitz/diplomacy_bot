# モジュールインポート
import discord

BOT_ACCESS_TOKEN = 'Njk4NzcxMDI1ODk4MjQyMDY4.XpKsNA.zSJIAwVm8WQabEjrCOhemo0MyzE'

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
