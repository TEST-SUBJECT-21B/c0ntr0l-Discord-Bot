import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Help")
    async def help(self, ctx):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title='Loading help',
            description=f'Loading help. If this does not progress, wait before trying again / restart the bot.',
            color=discord.Colour.green()
        )
        message = await ctx.channel.send(embed = embed)
        embed = discord.Embed(
            title='Help',
            description=f'Here is some help:',
            color=discord.Colour.green()
        )
        embed.add_field(
            name = "!Help",
            value = "Get some help",
            inline = True
        )
        embed.add_field(
            name = "!Kick <Member> <Reason>",
            value = "Kick a member",
            inline = False
        )
        embed.add_field(
            name = "!Ban <Member> <Reason>",
            value = "Ban a member",
            inline = True
        )
        embed.add_field(
            name = "!Unban <Member>",
            value = "Unban a member",
            inline = False
        )
        embed.add_field(
            name = "!Nuke <Optional Amount>",
            value = "Clear a channel",
            inline = True
        )
        message = await message.edit(embed = embed)


def setup(bot):
    bot.add_cog(Help(bot))
