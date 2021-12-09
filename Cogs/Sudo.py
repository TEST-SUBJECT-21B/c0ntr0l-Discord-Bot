import discord
import os
from discord.ext import commands


class Sudo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="Sudo", invoke_without_command=True)
    async def sudo(self, ctx):
        await ctx.channel.send("Enter a command to sudo.")
    
    @sudo.command()
    @commands.has_permissions(administrator=True)
    async def load_module(self, ctx, *, module):
        try:
            await self.bot.load_extension(f"Cogs.{module}")
        except Exception as E:
            await ctx.channel.send(f"Error invoking sudo load: {E}")
        
    @sudo.command()
    @commands.has_permissions(administrator=True)
    async def unload_module(self, ctx, *, module):
        try:
            self.bot.unload_extension(f"Cogs.{module}")
        except Exception as E:
            await ctx.channel.send(f"Error invoking sudo unload: {E}")

    @sudo.command()
    @commands.has_permissions(administrator=True)
    async def unload_all(self, ctx):
        try:
            for filename in os.listdir("./Cogs"):
                if filename.endswith('.py'):
                    self.bot.unload_extension(f"Cogs.{filename[:-3]}")
        except Exception as E:
            await ctx.channel.send(f"Error invoking sudo unload_all: {E}")
    
    @sudo.command()
    @commands.has_permissions(administrator=True)
    async def load_all(self, ctx):
            for filename in os.listdir("./Cogs"):
                if filename.endswith('.py') and not filename.startswith("_"):
                    self.bot.load_extension(f"Cogs.{filename[:-3]}")

    @sudo.command()
    @commands.has_permissions(administrator=True)
    async def kill(self, ctx):
        print(f"{ctx.author} called sudo kill")
        embed = discord.Embed(
            title = "Bye Bye",
            description = "The bot has been killed",
            color = discord.Colour.dark_gray()
        )
        await ctx.channel.send(embed = embed)
        os._exit(0)

    @sudo.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx):
        os.system('cls')
        print(f"{ctx.author} called sudo clear")
        await ctx.channel.send("The terminal log was cleared")
    
    @sudo.command()
    @commands.has_permissions(administrator=True)
    async def fnuke(self, ctx):
        await ctx.channel.purge(limit=999)


def setup(bot):
    bot.add_cog(Sudo(bot))