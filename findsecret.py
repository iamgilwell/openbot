import discord,random

client = discord.Client()

@client.event  #event decorator / wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):

     if message.content.startswith('hi there'):
        await client.send_message(message.channel, content = "Hello! \n How can I help you today?")

     elif message.content.startswith('flip'):
        flip=random.choice(["Heads","Tails"])
        await client.send_message(message.channel,(flip))

     elif message.content.startswith('need a quote'):
        await client.send_message(message.channel, content = "Sending you a quote shortly \n What is your email address?")

     elif message.content.startswith('service'):
        await client.send_message(message.channel, content = "Sending you a quote shortly \n What is your email address?")

    


    #'''print(f"{message.channel}:{message.author}:{message.author.name}:{message.content}") 

   
    #if "hi there" in message.content.lower():
    #   await client.send_message(message.channel, content = "Hello! \n How can I help you today?")

    #if "I need help" in message.content.lower():
     #  await client.send_message(message.channel, content = "Let me check,this might take a few minutes")'''




client.run("NTM2NzgxODU1OTU0MDQyODkw.Dybs8w.DZSrhZpMgjqszxJWaZEOxo8FBSg")