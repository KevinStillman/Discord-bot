import discord
from discord.ext import commands
import time
import random
import requests
import bs4
from bs4 import BeautifulSoup


version = "2.5"
def adminCheck(ctx):
    author = ctx.author
    adminRole = discord.utils.get(ctx.guild.roles, name="Admin")
    adminRole2 = discord.utils.get(ctx.guild.roles, name="Developer")
    if adminRole in author.roles or adminRole2 in author.roles:
        return True


class NormalCommands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def m(self, ctx, song):
        await ctx.send(f"m!play {song}")

    @commands.command()
    async def wom(self, ctx, username):
        await ctx.send(f"https://www.wiseoldman.net/players/{username}")

    @commands.command()
    async def ping(self,ctx):
        message = ctx.message
        await message.delete()
        await ctx.send(f"I have a latency of {round(self.client.latency*1000)}ms")

    @commands.command()
    async def version(self, ctx):
        message = ctx.message
        await message.delete()
        await ctx.send(f"Bot: v{version}")
        await self.client.delete_message()

    @commands.command()
    async def contributors(self, ctx):
        message = ctx.message
        await message.delete()
        await ctx.send("Below is the list of contributors to BadBot!")
        embed = discord.Embed(Color= discord.Colour.orange())
        embed.set_author(name="BadBot Contributors")
        embed.add_field(name="Kevin", value="Creator and Maintainer of BadBot", inline= True)
        await ctx.send(embed=embed)

    @commands.command()
    async def live(self, ctx, stream = None, streaming = None):
        message = ctx.message
        await message.delete()
        for channel in ctx.guild.channels:
            if channel.name == "twitch-notifications":
                Channel = channel
        if not stream and not streaming:
            await Channel.send("To use this command, use the following syntax:")
            await Channel.send("'.live [stream] [streaming]' where 'stream' is your stream name ")
            await Channel.send("and 'streaming' is an optional message of what you're streaming. (put 'streaming' in quotes)")
        else:
            if stream and not streaming:
                await Channel.send(f"@everyone Hey guys, {ctx.author.display_name} is live on twitch at https://www.twitch.tv/{stream}!")
            if stream and streaming:
                await Channel.send(f"@everyone Hey guys, {ctx.author.display_name} is live on twitch at https://www.twitch.tv/{stream} Streaming: {streaming}")

            await ctx.send("Make sure to check them out and give them a follow!")



    ################################### HELP BELOW ###################################
    @commands.command()
    async def help(self, ctx):
        message = ctx.message
        await message.delete()

        author = ctx.message.author
        embed = discord.Embed()

        if adminCheck(ctx):
            embed.set_author(name=f"BadBot Commands (Admin - Called by {ctx.author.display_name})")

            embed.add_field(name=".load", value="Takes in Cog name and Loads it", inline=False)
            embed.add_field(name=".reload", value="Takes in Cog name and Reloads it", inline=False)
            embed.add_field(name=".unload", value="Takes in Cog name and Unloads it", inline=False)
            embed.add_field(name=".clear", value="Takes in a number of chats to clear", inline=False)
            # Below this line, post the other commands from 'else' so they show when a normal role does .help

            embed.add_field(name=".live", value="Use this command to let the server know you're live streaming!", inline=False)
            embed.add_field(name=".update", value="Use this command to let the server know there's a game update, and optionally, how big the update is.", inline=False)
            embed.add_field(name=".help", value="This is Help", inline=False)
            embed.add_field(name=".ping", value="Returns Pong!", inline=False)
            embed.add_field(name=".version", value="Bot Version", inline=False)


            await ctx.send(embed=embed)
        else:
            embed.set_author(name=f"BadBot Commands (Normal member - Called by {ctx.author.display_name})")

            embed.add_field(name=".live", value="Use this command to let the server know you're live streaming!", inline=False)
            embed.add_field(name=".update", value="Use this command to let the server know there's a game update, and optionally, how big the update is.", inline=False)
            embed.add_field(name=".help", value="This is Help", inline=False)
            embed.add_field(name=".ping", value="Returns Pong!", inline=False)
            embed.add_field(name=".version", value="Bot Version", inline=False)

            await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(NormalCommands(client))
