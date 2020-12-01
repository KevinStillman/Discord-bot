import discord
import os
from discord.ext import commands
import time


class Background(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Loading...")
        time.sleep(3)
        print("Bot of Duty is Online!")
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("""Thank you for joining the discord server!
                          Please use the '/nick' command to change your username to your name on Call of Duty 
                          so we know who you are!""")
        for channel in member.guild.system_channel:
            if str(channel) == "welcome-channel":
                await channel.send(f"Welcome to the Server {member.mention}")

    @commands.Cog.listener()
    async def on_message(self, message):
#       Profanity filter
#         for files in os.listdir(".\Txtfiles"):
#             if files.startswith("profanity"):
#                 bad_words = open("profanity.txt", "r")
#         for badwords in bad_words.readlines():
#             if badwords in message.content.lower():
#                 print("Profanity found")
#                 await message.delete()
#                 await message.channel.send("Censored.")
        if "nigger" in message.content or "nigga" in message.content:
            await message.channel.send(f"Whoa there {message.author.display_name} we don't use that word.")
            await message.delete()

#       TeXaS?
        if "texas" in message.content.lower():
            if message.author.bot:
                return
            else:
                await message.channel.send(f" Hey {message.author.display_name} ¿?ArE yOu TeXaS¿?")





def setup(client):
    client.add_cog(Background(client))

