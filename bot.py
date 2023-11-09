import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command("help")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"Cogs.{extension}")
    for file in os.listdir("./Cogs"):
        if file.endswith(".py"):
            client.load_extension(f"Cogs.{file[:-3]}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"Cogs.{extension}")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"Cogs.{extension}")
    client.load_extension(f"Cogs.{extension}")
    print(f"Reload Finished by {ctx.author}")


@client.command()
async def botplaying(ctx, playing):
    await client.change_presence(activity=discord.Game(name=playing))


# ROLES

@client.event
async def on_reaction_add(reaction, user):
    print(f"{user} reacted with {reaction}")
    rolesChannel = client.get_channel(799757332057030666)

    # Location roles
    locationRoleIcons = ["🇺🇸", "🇪🇺", "🇺🇳"]
    locationRoleNames = ["Region - USA", "Region - EU", "Region - Other"]

    if reaction.emoji in locationRoleIcons:
        print(f"{user} reacted with a location role emoji")
        for role in user.roles:
            print(role)
            if role.name in locationRoleNames:
                print(f"prestige role '{role}' found")
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


token = "xlceUeJWVryZ_tzFBKWy6YCzdv_ZudZi"
client.run(token)
