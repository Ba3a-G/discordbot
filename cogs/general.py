# cogs/general.py

'''
General cog for commands.
'''


import disnake
from disnake import Option, OptionType
from disnake.ext import commands


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_before_slash_command_invoke(self, inter: disnake.CommandInteraction) -> None:
        await inter.response.defer(with_message=True)

    @commands.slash_command(
        name='greet',
        description='Greets a member.',
        options=[
            Option('member', 'Mention the server member you wish to greet.', OptionType.user, required=True)
        ]
    )
    async def _greet(self, inter: disnake.CommandInteraction, member: disnake.Member):
        await inter.send(f'Greetings, {member.mention}!')


def setup(bot):
    bot.add_cog(General(bot))
