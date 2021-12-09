import discord
from discord.ext import commands


class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Unban")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        await ctx.channel.purge(limit=1)
        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    return
            embed = discord.Embed(
                title="UNBAN!",
                description=f"{member} has been unbanned",
                color=discord.Colour.red()
            )
            await self.bot.get_guild(891670793187098644).get_channel(917066341255626813).send(embed=embed)
        except Exception as E:
            await ctx.channel.send(f"Error unbanning {member} : {E}")


def setup(bot):
    bot.add_cog(Unban(bot))