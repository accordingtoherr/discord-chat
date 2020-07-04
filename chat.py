import discord

client=discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("gosh"):
        await message.channel.send("napolean make youreself a dang quesidilla")
        if message.author == client.user:
            return
        if message.content.startswith("hi"):
            await message.channel.send("greetings, young one")
client.run('NzI4OTczMDgzNTUzMzAwNTYw.XwCLpw.qFqkZ5bXXpaaRu_UStePQd6ebbc')