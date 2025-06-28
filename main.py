import discord
import requests
import os

# Directly assign your values here
TOKEN = "MTM4ODUyMjQ0NDc2MzA0MTg1Mg.GCqoOE.LGtLJuJ4n5kr3CvR08ceBTbiuKtDyL41ZILjNM"
PUSHOVER_USER = "uv4qcecpiaw6v13k6xbshxrpa4mbw1"
PUSHOVER_TOKEN = "avx1eg2vhadsiu9j9x8tcarn1zjuyo"
TARGET_CHANNEL_ID = 1385387479410147411  # Make sure this is an integer

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def send_pushover_notification(message):
    requests.post("https://api.pushover.net/1/messages.json", data={
        "token": PUSHOVER_TOKEN,
        "user": PUSHOVER_USER,
        "message": message
    })

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.channel.id == TARGET_CHANNEL_ID and not message.author.bot:
        send_pushover_notification(f"{message.author}: {message.content}")

client.run(TOKEN)
