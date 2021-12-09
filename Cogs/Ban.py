import discord
from discord.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Ban")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member, *, reason: str):
        await ctx.channel.purge(limit=1)
        await member.ban(reason=reason)
        embed = discord.Embed(
            title = "BAN!",
            description = f"{member} has been banned for the reason {reason}",
            color = discord.Colour.red()
        )
        await self.bot.get_guild(891670793187098644).get_channel(917066341255626813).send(embed = embed)


def setup(bot):
    bot.add_cog(Ban(bot))
