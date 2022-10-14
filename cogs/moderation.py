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

    @commands.slash_command(
        name='invite',
        description='Get an invite link to this server.',
        dm_permission=False
    )
    async def _invite(self, inter: disnake.CommandInter) -> None:
        invite = await inter.channel.create_invite(max_age=0, max_uses=0)
        await inter.send(f'Here\'s an invite link to this server: https://discord.gg/{invite.code}')


def setup(bot):
    bot.add_cog(Moderation(bot))
