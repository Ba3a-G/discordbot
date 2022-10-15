# cogs/moderation.py

"""
Moderation cog for commands.
"""


import disnake
from disnake import Option, OptionType
from disnake.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name="ban",
        description="Bans people.",
        options=[
            Option(
                "member",
                "The server member you want to ban.",
                OptionType.user,
                required=True,
            ),
            Option("reason", "Reason for banning the person.", OptionType.string),
        ],
        default_member_permissions=disnake.Permissions(ban_members=True),
        dm_permission=False,
    )
    async def _ban(
        self,
        inter: disnake.CommandInter,
        member: disnake.Member,
        reason: str | None = None,
    ) -> None:
        await inter.guild.ban(member, reason=reason)
        await inter.send(f"Banned {member.name}{member.discriminator}!")

    @commands.slash_command(
        name="sofban",
        description="Softans people to wipe their messages.",
        options=[
            Option(
                "member",
                "The server member you want to ban.",
                OptionType.user,
                required=True,
            ),
            Option("reason", "Reason for softbanning the person.", OptionType.string),
        ],
        default_member_permissions=disnake.Permissions(ban_members=True),
        dm_permission=False,
    )
    async def _softban(
        self,
        inter: disnake.CommandInter,
        member: disnake.Member,
        reason: str | None = None,
    ) -> None:
        await inter.guild.ban(member, reason=reason, delete_message_days=7)
        await inter.send(f"Softbanned {member.name}{member.discriminator}!")

    @commands.slash_command(
        name="unban",
        description="Unbans a member from the server.",
        options=[
            Option(
                "member",
                "The server member you'd like to unban.",
                OptionType.user,
                required=True,
            )
        ],
        default_member_permissions=disnake.Permissions(ban_members=True),
        dm_permission=False,
    )
    async def _unban(self, inter: disnake.CommandInter, member: disnake.Member) -> None:
        await inter.guild.unban(member)
        await inter.send(f"Unbanned {member.display_name}!")

    @commands.slash_command(
        name="kick",
        description="Kicks a member from the server.",
        options=[
            Option(
                "member",
                "The server member you'd like to kick.",
                OptionType.user,
                required=True,
            ),
            Option("reason", "Reason for kicking the person.", OptionType.string),
        ],
        default_member_permissions=disnake.Permissions(kick_members=True),
        dm_permission=False,
    )
    async def _kick(
        self,
        inter: disnake.CommandInter,
        member: disnake.Member,
        reason: str = "No reason provided.",
    ) -> None:
        await inter.guild.kick(member, reason=reason)
        await inter.send(f"Kicked {member.name}{member.discriminator}!")


def setup(bot):
    bot.add_cog(Moderation(bot))
