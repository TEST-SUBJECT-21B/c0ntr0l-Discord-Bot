import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Ping")
    async def ping(self, ctx):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='Pong',
            description=f'I\'m up and running',
            color=discord.Colour.green()
        )
        embed.add_field(
            name = "Latency",
            value = f"{round(self.bot.latency * 100, 3)}ms",
            inline = True
        )
        embed.set_thumbnail(url="https://www.evomontreal.com/wp-content/uploads/2015/04/ping-pong.jpg")
        await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Ping(bot))