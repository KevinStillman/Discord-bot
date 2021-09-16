import discord
from discord.ext import commands
import time

version = "0.3.1"

def adminCheck(ctx):
    author = ctx.author
    adminRole = discord.utils.get(ctx.guild.roles, name="Owner")
    adminrole2 = discord.utils.get(ctx.guild.roles, name="Admiral")
    adminrole3 = discord.utils.get(ctx.guild.roles, name="Colonel")
    adminrole4 = discord.utils.get(ctx.guild.roles, name="Commander")
    adminrole5 = discord.utils.get(ctx.guild.roles, name="Officer")
    adminrole6 = discord.utils.get(ctx.guild.roles, name="ADMIN")
    if adminRole in author.roles or adminrole2 in author.roles or adminrole3 in author.roles or adminrole4 in author.roles or adminrole5 in author.roles or adminrole6 in author.roles:
        return True


class NormalCommands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self,ctx):
        message = ctx.message
        await message.delete()
        await ctx.send(f"Literal Bot has a latency of {round(self.client.latency*1000)}ms")

    @commands.command()
    async def version(self, ctx):
        message = ctx.message
        await message.delete()
        await ctx.send(f"Literal Bot Current Version: v{version}")
        await self.client.delete_message()

    @commands.command()
    async def contributors(self, ctx):
        message = ctx.message
        await message.delete()
        await ctx.send("Below is the list of contributors to PyBot!")
        embed = discord.Embed(Color= discord.Colour.orange())
        embed.set_author(name="Literal Bot Contributors")
        embed.add_field(name="Kevin", value="Creator and Maintainer of Literal Bot", inline= True)
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


    @commands.command()
    async def live(self, ctx, stream = None, streaming = None):
        message = ctx.message
        await message.delete()
        for channel in ctx.guild.channels:
            if channel.name == "shoutouts":
                Channel = channel
        if not stream and not streaming:
            await Channel.send("To use this command, use the following syntax:")
            await Channel.send("'.live [stream] [streaming]' where 'stream' is your stream name ")
            await Channel.send("and 'streaming' is an optional message of what you're streaming. (put 'streaming' in quotes)")
        else:
            if stream and not streaming:
                await Channel.send(f"@here Hey guys, {ctx.author.display_name} is live on twitch at https://www.twitch.tv/{stream}!")
            if stream and streaming:
                await Channel.send(f"@here Hey guys, {ctx.author.display_name} is live on twitch at https://www.twitch.tv/{stream} Streaming: {streaming}")

            await channel.send("Make sure to check them out and give them a follow!")


    ################################### HELP BELOW ###################################
    @commands.command()
    async def help(self, ctx):
        message = ctx.message
        await message.delete()

        author = ctx.message.author
        embed = discord.Embed(Color=discord.Colour.orange())

        if adminCheck(ctx):
            embed.set_author(name=f"Literal Bot Commands (Admin - Called by {ctx.author.display_name})")

            embed.add_field(name=".load", value="Takes in Cog name and Loads it", inline=False)
            embed.add_field(name=".reload", value="Takes in Cog name and Reloads it", inline=False)
            embed.add_field(name=".unload", value="Takes in Cog name and Unloads it", inline=False)
            embed.add_field(name=".clear", value="Takes in a number of chats to clear", inline=False)
            embed.add_field(name=".ban", value="HAMMER TIME", inline=False)

            # Below this line, post the other commands from 'else' so they show when a normal role does .help
            embed.add_field(name=".help", value="This is Help", inline=False)
            embed.add_field(name=".ping", value="Returns Pong!", inline=False)
            embed.add_field(name=".version", value="Bot Version", inline=False)
            embed.add_field(name=".suggest", value="Used to suggest a function for the bot", inline=False)


            await ctx.send(embed=embed)

        else:
            embed.set_author(name=f"Literal Bot Commands (Normal member - Called by {ctx.author.display_name})")

            embed.add_field(name=".live", value="Use this command to let the server know you're live streaming!", inline=False)
            embed.add_field(name=".help", value="This is Help", inline=False)
            embed.add_field(name=".ping", value="Returns Pong!", inline=False)
            embed.add_field(name=".version", value="Bot Version", inline=False)
            embed.add_field(name=".suggest", value="Used to suggest a function for the bot", inline=False)

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(NormalCommands(client))
