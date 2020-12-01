import discord
from discord.ext import commands
from discord.ext.commands import has_role, CheckFailure

class AdminCommands(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command()
    async def clear(self, ctx, amount=5):
        message = ctx.message
        await message.delete()
        admin = discord.utils.get(ctx.guild.roles, name="Admin")
        developer = discord.utils.get(ctx.guild.roles, name="Developer")
        if admin or developer in ctx.author.roles:
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send(f"You don't have permission to use that command!{ctx.message.author.mention}")


    @commands.command()
    async def ban(self, ctx, who, reason):
        message = ctx.message
        await message.delete()
        pass # Will fill this in, just allowing for now to run the bot


def setup(client):
    client.add_cog(AdminCommands(client))
