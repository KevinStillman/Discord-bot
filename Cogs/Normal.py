import discord
from discord.ext import commands
import time

version = "2.4.1"



class NormalCommands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self,ctx):
        message = ctx.message
        await message.delete()
        await ctx.send(f"Bot of Duty has a latency of {round(self.client.latency*1000)}ms")

    @commands.command()
    async def version(self, ctx):
        message = ctx.message
        await message.delete()
        await ctx.send(f"Bot of Duty Current Version: v{version}")
        await self.client.delete_message()

    @commands.command()
    async def contributors(self, ctx):
        message = ctx.message
        await message.delete()
        await ctx.send("Below is the list of contributors to PyBot!")
        embed = discord.Embed(Color= discord.Colour.orange())
        embed.set_author(name="Bot of Duty Contributors")
        embed.add_field(name="Kevin", value="Creator and Maintainer of Bot of Duty", inline= True)
        embed.add_field(name="Adam", value="Reworked Bot to include cogs", inline= True)
        await ctx.send(embed=embed)

    @commands.command()
    async def suggest(self, ctx, suggestion):
        message = ctx.message
        await message.delete()
        suggestion = str(suggestion)
        suggestionfile = open("suggestions.txt", "a")
        suggestionfile.write(suggestion + "\n")
        suggestionfile.close()
        await ctx.send(f"Your suggestion of '{suggestion}' has been sent.")

        #   #   #   #   WORK ON THIS COMMAND WHEN IMPLEMENTATION IS THOUGHT THROUGH #   #   #   #
    @commands.command()
    async def mvpexample(self, ctx, kills):
        who = ctx.author

        embed = discord.Embed(color = discord.Colour.orange())
        embed.set_author(name="Server Leaderboard")

        embed.add_field(name = "MVP", value = "Kevin")
        embed.add_field(name= "Kills", value = kills)

        embed.add_field(name = "2nd Place", value = "x")

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

    @commands.command()
    async def update(self, ctx, size=None):
        message = ctx.message
        await message.delete()
        for channel in ctx.guild.channels:
            if channel.name == "announcements":
                if not size:
                    await channel.send("@everyone \nThere is an update for Black Ops Cold War! Make sure you update your game!")
                if size:
                    await channel.send(f"@everyone \nThere is an update for Black Ops Cold War! The update is {size}gb, make sure you update your game! ")




    ################################### HELP BELOW ###################################
    @commands.command()
    async def help(self, ctx):
        message = ctx.message
        await message.delete()
        adminRole=discord.utils.get(ctx.guild.roles, name="Admin")
        adminRole += "Developer"
        author = ctx.message.author
        embed = discord.Embed(Color=discord.Colour.orange())
        
        if adminRole in ctx.author.roles:
            embed.set_author(name="Bot of Duty Commands (Admin)")

            embed.add_field(name=".load", value="Takes in Cog name and Loads it", inline=False)
            embed.add_field(name=".reload", value="Takes in Cog name and Reloads it", inline=False)
            embed.add_field(name=".unload", value="Takes in Cog name and Unloads it", inline=False)
            embed.add_field(name=".clear", value="Takes in a number of chats to clear", inline=False)
            embed.add_field(name=".live", value="Use this command to let the server know you're live streaming!", inline=False)
            embed.add_field(name=".update", value="Use this command to let the server know there's a game update, and optionally, how big the update is.", inline=False)
            embed.add_field(name=".help", value="This is Help", inline=False)
            embed.add_field(name=".ping", value="Returns Pong!", inline=False)
            embed.add_field(name=".version", value="Bot Version", inline=False)
            embed.add_field(name=".suggest", value="Used to suggest a function for the bot", inline=False)
            # Below this line, post the other commands from 'else' so they show when a normal role does .help



            await ctx.send(embed=embed)
        else:
            embed.set_author(name="Bot of Duty Commands")

            embed.add_field(name=".live", value="Use this command to let the server know you're live streaming!", inline=False)
            embed.add_field(name=".update", value="Use this command to let the server know there's a game update, and optionally, how big the update is.", inline=False)
            embed.add_field(name=".help", value="This is Help", inline=False)
            embed.add_field(name=".ping", value="Returns Pong!", inline=False)
            embed.add_field(name=".version", value="Bot Version", inline=False)
            embed.add_field(name=".suggest", value="Used to suggest a function for the bot", inline=False)

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(NormalCommands(client))
