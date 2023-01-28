# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = "@"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startwith(prefix):
        if message.content == prefix + "hello":
            await message.channel.send("hello there!")

client.run('MTA2ODg4ODM0Njk3OTQ3NTQ2Ng.GPQcd5.74gjkIFs8HJd0UX9n-lHWAFupRLKUrRM7M5Hs4')
