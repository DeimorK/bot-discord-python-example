# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client. event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if '!davi' in message.content.lower():
        await message.channel.send('GRANDE REI DAVI :crown:')

    if '!matrix' in message.content.lower():
        await message.channel.send('Davi é o salvador e irá derrotar a Matrix')
        
    if '!help' in message.content.lower():
        await message.channel.send('Use "!" antes do comando: \n\nComandos:\ndavi')

client.run(TOKEN)
