# cogs/general.py

'''
General cog for commands.
'''

import discord
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='greet', help='Greets members.')
    async def _greet(self, ctx: commands.Context, member: discord.Member):
        await ctx.send(f'Greetings, {member.mention}!')


def setup(bot):
    bot.add_cog(General(bot))