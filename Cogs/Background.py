import discord
import os
from discord.ext import commands
import time

import random

lovenotes = ["I fucking love you so hard...",
            "You've got a nice big juicy cock, sir",
            "Spank me daddy",
            "You have a funny feeling you would've been followed...",
            "imagine not being 126 lmao fucking noob",
            "Make me a sandwich.",
            "Service yourself, fucking loser",
            "Are you texus!?",
            "beast sucks anus",
            "Imagine having a shadow and sucking at wardens",
            "Imagine, imagining",
            "You know why they call him muff right? Cause he's a bitch."
            "lol scammed, fucking idiot",
            "I fucked your account, sorry...",
            "imagine playing leagues lol"
]


class Background(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("BadBot is Online!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("""Thank you for joining the discord server! For a full list of bot commands, type '.help'
                          Please Read the rules and let an admin know if you have any questions!""")

    @commands.command()
    async def vc(self, ctx):
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('shit.mp4', executable="C:/ffmpeg/bin/ffmpeg.exe"), after=lambda e: print('done', e) )


    @commands.Cog.listener()
    async def on_message(self, message):
#   TEXT LOGGING
        print(f"[{message.channel}] {message.author.display_name}: {message.content}")
#   PROFANITY FILTER
        if "nigger" in message.content.lower() or "nigga" in message.content.lower():
                await message.channel.send(f"Whoa there {message.author.display_name} we don't use that word.")
                await message.delete()
                with open('cat.jpg', 'rb') as f:
                    picture = discord.File(f)
                    await message.channel.send(file=picture)

#       random bot call?
        if " bot" in message.content.lower() or "bot " in message.content.lower():
            if message.author.bot:
                return
            else:
                await message.channel.send(random.choice(lovenotes))

        if message.author.display_name == "Johan":
            x = random.choice(range(10))
            if x < 3:
                print(f"RNG CHECK! \n{message}")
                await message.channel.send("Johan... who let you out of the cage?")

        if message.author.display_name == "Rav en":
            x = random.choice(range(20))
            if x < 3:
                print(f"RNG CHECK! \n{message}")
                await message.channel.send("Raven is here? Must be leagues season")

        if message.author.display_name == "BeastlyMuff":
            z = random.choice(range(6))
            if z == 1:
                if message.content.startswith("m!play"):
                    print(f"RNG CHECK! \n{message}")
                    await message.channel.send("Everyone ready for another garbage song?")

        if message.author.display_name == "Ethun":
            y = random.choice(range(10))
            if y < 2:
                print(f"RNG CHECK! \n{message}")
                await message.channel.send("Eventually i'll write something here to piss you off")

        if message.author.display_name == "A Witch Dr":
            y = random.choice(range(10))
            if y < 2:
                print(f"RNG CHECK! \n{message}")
                await message.channel.send("Oh shit the leagues sweatmeister is talking")

        elif message.content.startswith('???'):  # Saying ??? will make bot leave channel
            if (message.guild.voice_client):  # If the bot is in a voice channel
                await message.guild.voice_client.disconnect()  # Leave the channel
                # await message.channel.send('Bot left')
async def setup(client):
    await client.add_cog(Background(client))
