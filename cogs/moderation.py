# cogs/moderation.py

'''
Moderation cog for commands.
'''


import disnake
from disnake import Option, OptionType
from disnake.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name='ban',
        description='Bans people.',
        options=[
            Option(
                'member',
                'The server member you want to ban.',
                OptionType.user,
                required=True
            ),
            Option(
                'reason',
                'Reason for banning the person.',
                OptionType.string
            )
        ]
    )
    async def _ban(self, inter: disnake.CommandInter, member: disnake.Member,
                   reason: str | None = None) -> None:
        await inter.guild.ban(member, reason=reason)
        await inter.send(f'Banned {member.name}{member.discriminator}!')


def setup(bot):
    bot.add_cog(Moderation(bot))
