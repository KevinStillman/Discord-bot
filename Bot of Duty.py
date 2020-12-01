import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = commands.Bot(command_prefix='.', intents=intents)
client.remove_command("help")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"Cogs.{extension}")


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

for file in os.listdir("./Cogs"):
    if file.endswith(".py"):
        client.load_extension(f"Cogs.{file[:-3]}")

# ROLES

@client.event
async def on_reaction_add(reaction, user):
    print(f"{user} reacted with {reaction}")
    rolesChannel = client.get_channel(779388025289310259)
    # prestige roles
    prestigeRoleIcons = ["1️⃣", "2️⃣", "3️⃣", "☠"]
    prestigeRoles = ["1st Prestige", "2nd Prestige", "3rd Prestige", "MAX Prestige"]

    if reaction.emoji in prestigeRoleIcons:
        print(f"{user} reacted with a prestige role emoji")
        for role in user.roles:
            print(role)
            if role.name in prestigeRoles:
                print(f"prestige role '{role}' found")
                await user.remove_roles(role)
    ##       No prestige
    if reaction.emoji == "💩":
        Role = discord.utils.get(user.guild.roles, name="No Prestige")
        await user.add_roles(Role)
    ##       1st prestige
    if reaction.emoji == "1️⃣":
        Role = discord.utils.get(user.guild.roles, name="1st Prestige")
        await user.add_roles(Role)
    ##       2nd prestige
    if reaction.emoji == "2️⃣":
        Role = discord.utils.get(user.guild.roles, name="2nd Prestige")
        await user.add_roles(Role)
    ##       3rd prestige
    if reaction.emoji == "3️⃣":
        Role = discord.utils.get(user.guild.roles, name="3rd Prestige")
        await user.add_roles(Role)
    ##       MAX prestige
    if reaction.emoji == "💀":
        Role = discord.utils.get(user.guild.roles, name="MAX Prestige")
        await user.add_roles(Role)


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


token = "Nzc3ODkxNDc3MzEyODk3MDM1.X7KB5A.AwWWaKs3Zazeeu-w65kfkpyvXrM"
client.run(token)
