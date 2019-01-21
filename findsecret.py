import discord

client = discord.Client()

@client.event  #event decorator / wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel}:{message.author}:{message.author.name}:{message.content}") 

    if "hi there" in message.content.lower():
       await message.channel.send('Hi!')


client.run("NTM2NzgxODU1OTU0MDQyODkw.Dybs8w.DZSrhZpMgjqszxJWaZEOxo8FBSg")