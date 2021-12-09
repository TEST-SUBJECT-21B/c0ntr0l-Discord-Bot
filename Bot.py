import discord
import os
import time
from discord.ext import commands

# Create bot and remove !help, to make way for !Help
bot = commands.Bot(command_prefix = "!")
bot.remove_command("help")

# botData, for verbose debugging in the debug file
global botData
botData = (
    f"Name: c0ntr0l", 
    f"User: c0ntr0l#9055", 
    f"Main_file: Bot.py",
    f"Token_file: Token.txt",
    f"Cogs_dir: ./Cogs",
    f"Debug_cog: Cogs._Sudo",
    f"Cog_dir: {os.listdir('./Cogs')}"
)

# Loading helper commands
async def unload_all():
    for filename in os.listdir("./Cogs"):
        if filename.endswith('.py'):
            bot.unload_extension(name = f"Cogs.{filename[:-3]}")

async def load_all():
    for filename in os.listdir("./Cogs"):
        if filename.endswith('.py') and not filename.startswith("_"):
            bot.load_extension(name = f"Cogs.{filename[:-3]}")

async def load(ctx, *, ext):
    await bot.load_extension(name = f"Cogs.{ext}")

async def unload(ext):
    bot.unload_extension(name = f"Cogs.{ext}")

async def reload(ext):
    await unload(ext)
    await load(ext)


# Bot events
@bot.event
async def on_ready():
    os.system('cls')
    print(f"Logged in as {bot.user}\n")
    print("Initialised commands:")
    await load_all()
    for filename in os.listdir("./Cogs"):
        if filename.endswith('.py') and not filename.startswith('_'):
            print(f"\tLoaded command {filename[:-3]}")
    print("\n")
    await bot.change_presence(activity = discord.Game("!Help for help"), status="Online")
    print("Bot status changed:")
    print("\tStatus = Online")
    print("\tActivity = !Help for help")
    print("\n")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title = "You numpty",
            description = "Finish the command, you numpty",
            color = discord.Colour.dark_gray()
        )
        await ctx.channel.send(embed = embed)
    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title = "Wot",
            description = "No clue what you're on about, mate",
            color = discord.Colour.dark_gray()
        )
        await ctx.channel.send(embed=embed)
    else:
        pass


# Bot commands
@bot.command()
async def Load(ctx, extention):
    await ctx.channel.send(f"Loaded module {extention}")
    print(f"Loaded module {extention}")
    await load(extention)
 
@bot.command()
async def Unload(ctx, extention):
    await ctx.channel.send(f"Unloaded module {extention}")
    print(f"Unloaded module {extention}")
    await unload(extention)

@bot.command()
async def Reload(ctx, extention):
    await reload(extention)

@bot.command()
async def Restart(ctx):
    embed = discord.Embed(
        title = "Reloading all cogs",
        description = "All cogs are being reloaded",
        color = discord.Colour.green()
    )
    for ext in os.listdir("./Cogs"):
        if ext.endswith(".py") and not ext.startswith("_"):
            try:
                bot.unload_extension(f"Cogs.{ext[:-3]}")
                bot.load_extension(f"Cogs.{ext[:-3]}")
                embed.add_field(
                    name = f"Reloaded: `{ext}`",
                    value = "--------------------------",
                    inline=False
                )
            except Exception as E:
                embed.add_field(
                    name = f"Failed to reload: `{ext}`",
                    value="--------------------------",
                    inline = False
                )
                pass
    
    embed.add_field(
        name=f"Done",
        value="Completed reload",
        inline=False
    )
    await ctx.channel.send(embed = embed)
    print("Bot has restarted")

# Read the token from token.txt
TokenFile = open("Token.txt", "r")
Token = TokenFile.readline()
TokenFile.close()

# Login
bot.run(Token)