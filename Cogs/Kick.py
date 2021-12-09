import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Kick")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason: str):
        await ctx.channel.purge(limit=1)
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="KICK!",
            description=f"{member} has been Kicked for: {reason}",
            color=discord.Colour.red()
        )
        await self.bot.get_guild(891670793187098644).get_channel(917066341255626813).send(embed=embed)


def setup(bot):
    bot.add_cog(Kick(bot))
