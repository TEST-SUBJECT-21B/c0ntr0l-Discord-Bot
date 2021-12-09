import discord
import time
from discord.ext import commands


class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Nuke")
    @commands.has_permissions(manage_messages = True)
    async def nuke(self, ctx, amount=999):
        embed = discord.Embed(
            title="Loading",
            description="Loading nuke...",
            color=discord.Colour.red(),
        )
        message = await ctx.channel.send(embed=embed)
        embed = discord.Embed(
            title="BOOM",
            description="Nuking in 3...",
            color=discord.Colour.red(),
            footer=f"Nuke requested by {ctx.author.name}"
        )
        embed.set_thumbnail(url="https://imgr.search.brave.com/1V34MgbYFQ1hoRcMFgGH5lXPcq4ZvXhdRoHDyvYJyGo/fit/632/225/ce/1/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5R/VVJuaVZlZEEzRWI3/SFBZMmlUQUtnSGFG/aiZwaWQ9QXBp")
        await message.edit(embed=embed)
        time.sleep(1)
        embed = discord.Embed(
            title="BOOM",
            description="Nuking in 2...",
            color=discord.Colour.red(),
            footer=f"Nuke requested by {ctx.author.name}"
        )
        embed.set_thumbnail(url="https://imgr.search.brave.com/1V34MgbYFQ1hoRcMFgGH5lXPcq4ZvXhdRoHDyvYJyGo/fit/632/225/ce/1/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5R/VVJuaVZlZEEzRWI3/SFBZMmlUQUtnSGFG/aiZwaWQ9QXBp")
        await message.edit(embed=embed)
        time.sleep(1)
        embed = discord.Embed(
            title="BOOM",
            description="Nuking in 1...",
            color=discord.Colour.red(),
            footer=f"Nuke requested by {ctx.author.name}"
        )
        embed.set_thumbnail(url="https://imgr.search.brave.com/1V34MgbYFQ1hoRcMFgGH5lXPcq4ZvXhdRoHDyvYJyGo/fit/632/225/ce/1/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5R/VVJuaVZlZEEzRWI3/SFBZMmlUQUtnSGFG/aiZwaWQ9QXBp")
        await message.edit(embed=embed)
        time.sleep(1)
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=(amount+1))


def setup(bot):
    bot.add_cog(Nuke(bot))