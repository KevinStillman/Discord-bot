import discord
from discord.ext import commands
import os
from datetime import datetime
intents = discord.Intents.all()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command("help")

botstarttime = datetime.now()


@client.command()
async def uptime(ctx):
    await ctx.send(f"The Bot has been online since {botstarttime}, eventually i'll be able to tell you how long that's been.")
@client.command()
async def load(ctx, extension):
    client.load_extension(f"Cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"Cogs.{extension}")
    channel = client.get_channel()

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"Cogs.{extension}")
    client.load_extension(f"Cogs.{extension}")
    print(f"Reload Finished by {ctx.author}")

@client.command()
async def botplaying(ctx, playing):
    await client.change_presence(activity=discord.Game(name=playing))

@client.command()
async def run(ctx):
    needroles = False
    #temporary admin check
    if ctx.author.display_name == "BeastlyMuff - JB" or ctx.author.display_name == "Kevin - Ciwa" or ctx.author.display_name == "Johan":
        for file in os.listdir("./Cogs"):
            if file.endswith(".py"):
                await client.load_extension(f"Cogs.{file[:-3]}")
        #check if anyone needs roles
        role = discord.utils.find(lambda r: r.name == 'member', ctx.message.guild.roles)
        for member in ctx.guild.members:
            if role in member.roles:
                print(f"{role} found for {ctx.member}: {member.roles}")
            else:
                needroles = True
        if needroles:
            channel = client.get_channel(1177277807861182596)
            await channel.send("Someone needs a role")
        needroles = False
    else:
        pass



    await ctx.send("BadBot online! For a list of current commands, type .help")


# ROLES -- Currently left out until further implementation inside the discord is setup

@client.event
async def on_reaction_add(reaction, user):
    print(f"{user} reacted with {reaction}")
    rolesChannel = client.get_channel(779388025289310259)

    # Location roles
    locationRoleIcons = ["🇺🇸", "🇪🇺", "🇺🇳"]
    locationRoleNames = ["Region - USA", "Region - EU", "Region - Other"]

    if reaction.emoji in locationRoleIcons:
        print(f"{user} reacted with a location role emoji")
        for role in user.roles:
            print(role)
            if role.name in locationRoleNames:
                print(f" role '{role}' found")
                await user.remove_roles(role)

    # USA
    if reaction.emoji == "🇺🇸":
        Role = discord.utils.get(user.guild.roles, name="Region - USA")
        await user.add_roles(Role)
    # EU
    if reaction.emoji == "🇪🇺":
        Role = discord.utils.get(user.guild.roles, name="Region - EU")
        await user.add_roles(Role)
    # Other
    if reaction.emoji == "🇺🇳":
        Role = discord.utils.get(user.guild.roles, name="Region - Other")
        await user.add_roles(Role)


with open("token.txt", "r") as tokenfile:
    token = tokenfile.readline()
client.run(token)

