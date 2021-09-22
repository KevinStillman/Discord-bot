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
        print("UGN Bot is Online!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("""Thank you for joining the discord server! For a full list of bot commands, type '.help'
                          Please Read the rules and let an admin know if you have any questions!""")
        for channel in member.guild.system_channel:
            if str(channel) == "welcome-channel":
                await channel.send(f"Welcome to the Server {member.mention}")

    @commands.Cog.listener()
    async def on_message(self, message):
#   TEXT LOGGING
        print(f"[{message.channel}] {message.author.display_name}: {message.content}")
#   PROFANITY FILTER
        if "nigger" in message.content or "nigga" in message.content:
            await message.channel.send(f"Whoa there {message.author.display_name} we don't use that word.")
            await message.delete()

#       TeXaS?
        if "texas" in message.content.lower():
            if message.author.bot:
                return
            else:
                await message.channel.send(f" Hey {message.author.display_name} ¿?ArE yOu TeXaS¿?")

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     #   TEXT LOGGING
    #     print(f"[{message.channel}] {message.author.display_name}: {message.content}")
    #
    #     # profanity filter FROM FILE
    #     for file in os.listdir("Txtfiles"):
    #         if file == "profanity.txt":
    #             profanityFile = open(file, "r")
    #
    #     for line in profanityFile.readline():
    #         if message.content in profanityFile:
    #             await message.delete
    #             await message.channel.send(
    #                 "Hey there {message.author.display_name}, we don't use that word around here.")


def setup(client):
    client.add_cog(Background(client))
