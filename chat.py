import discord

client=discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("gosh"):
        await message.channel.send("napolean make youreself a dang quesidilla")
    if message.content.startswith("your mom"):
        await message.channel.send("goes to college!")
    else:
        await message.channel.send("you IDIOT")

client.run('')