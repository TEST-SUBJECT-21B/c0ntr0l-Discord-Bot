import discord
from discord.ext import commands


class SecretAchievements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Sus")
    async def sus(self, ctx):
        embed = discord.Embed(
            title = "SUS",
            description = "SUS AMOG US",
            color = discord.Colour.red()
        )
        embed.set_thumbnail(url="https://emojis.slackmojis.com/emojis/images/1605479284/10796/among_us_party.gif?1605479284")
        await ctx.channel.send(embed=embed)
    
    @commands.command(name="Poo")
    async def poo(self, ctx):
        embed = discord.Embed(
            title="POO",
            description="HAHAHA POO HAAHAHA STINKY POO HAHA TOILET POO AHAHAHAHAHAH",
            color=discord.Colour.red()
        )
        embed.set_thumbnail(url="https://www.emp.co.uk/dw/image/v2/BBQV_PRD/on/demandware.static/-/Sites-master-emp/default/dw8cf8d57b/images/3/5/8/7/358763a2-emp.jpg?sfrm=png")
        await ctx.channel.send(embed = embed)
        await ctx.channel.send("I'm suuuuuuu-ing you.")


def setup(bot):
    bot.add_cog(SecretAchievements(bot))
