# This example requires the 'message_content' intent.

import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = "<"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        if message.content == prefix + "help":
            menu = """
            Menu:
            <hello - Says hello
            <rps - play rock papper scissors with bot by using command <rps [your_choice]
            """
            await message.channel.send(menu)   

    if message.content.startswith(prefix):
        if message.content == prefix + "hello":
            await message.channel.send("Hello there!")

    if message.content.startswith("<rps"):
        options = ["rock", "paper", "scissors"]
        bot_choice = random.choice(options)
        user_choice = message.content.split(" ")[1].lower()
        if user_choice in options:
            if user_choice == bot_choice:
                await message.channel.send(f"It's a tie! I chose {bot_choice}.")
            elif (user_choice == "rock" and bot_choice == "scissors") or (user_choice == "paper" and bot_choice == "rock") or (user_choice == "scissors" and bot_choice == "paper"):
                await message.channel.send(f"You win! I chose {bot_choice}.")
            else:
                await message.channel.send(f"I win! I chose {bot_choice}.")
        else:
            await message.channel.send("Invalid choice, please choose rock, paper, or scissors.")    

client.run('token goes here!')
