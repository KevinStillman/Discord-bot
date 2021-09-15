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
        print("Literal Bot is Online!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("""Thank you for joining the discord server! For a full list of bot commands, type '.help'
                          Please Read the rules and let an admin know if you have any questions!
                          Please also change your discord name to reflect your ingame name using /nick""")


    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"[{message.channel}] {message.author.display_name}: {message.content}")
#       Profanity filter

        if "nigger" in message.content or "nigga" in message.content:
            await message.channel.send(f"Whoa there {message.author.display_name} we don't use that word.")
            await message.delete()

def setup(client):
    client.add_cog(Background(client))
