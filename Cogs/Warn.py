import discord
from discord.ext import commands


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Warn")
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason: str):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title="Warning!",
            description=f"You have been warned by {ctx.message.author} for: {reason}",
            color=discord.Colour.red()
        )
        await member.send(embed = embed)
        embed = discord.Embed(
            title="Warning!",
            description=f"{member} has been warned by {ctx.message.author} for: {reason}",
            color=discord.Colour.red()
        )
        await self.bot.get_guild(891670793187098644).get_channel(917066341255626813).send(embed=embed)


def setup(bot):
    bot.add_cog(Warn(bot))