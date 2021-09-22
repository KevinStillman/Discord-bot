import discord
from discord.ext import commands
from discord.ext.commands import has_role, CheckFailure


def adminCheck(ctx):
    author = ctx.author
    adminRole = discord.utils.get(ctx.guild.roles, name="Admin")
    adminRole2 = discord.utils.get(ctx.guild.roles, name="Developer")
    if adminRole in author.roles or adminRole2 in author.roles:
        return True



class AdminCommands(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command()
    async def clear(self, ctx, amount=5):
        message = ctx.message
        await message.delete()

        if adminCheck(ctx):
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.send(f"You don't have permission to use that command!{ctx.message.author.mention}")


    @commands.command()
    async def ban(self, ctx, who = None, reason = None):
        message = ctx.message
        await message.delete()
        if not who or not reason:
            await ctx.send("""To use this command, you MUST include a name and a reason for ban. Please retry with the following:"
                           .ban [who] [reason]
                           """)
        else:

            if adminCheck(ctx):
                await ctx.send(f"GET THE HAMMER {who}!")
                pass # Will fill this in, just allowing for now to run the bot
            else:
                await ctx.send(f"Hey guys, {ctx.author} just tried to do something very silly!")


def setup(client):
    client.add_cog(AdminCommands(client))
