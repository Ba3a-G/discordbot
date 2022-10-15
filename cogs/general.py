# cogs/general.py

"""
General cog for commands.
"""


import disnake
from disnake import Option, OptionType
from disnake.ext import commands


class HelpView(disnake.ui.View):
    def __init__(self, *, timeout: float = 180) -> None:
        super().__init__(timeout=timeout)

        self.add_item(
            disnake.ui.Button(
                label="My Source Code",
                style=disnake.ButtonStyle.link,
                url="https://github.com/taotnpwaft/discordbot",
            )
        )
        self.add_item(
            disnake.ui.Button(
                label="The Art of Tech | GitHub",
                style=disnake.ButtonStyle.link,
                url="https://github.com/taotnpwaft",
            )
        )


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_before_slash_command_invoke(
        self, inter: disnake.CommandInter
    ) -> None:
        await inter.response.defer()

    @commands.slash_command(name="help", description="Get to know me!")
    async def _help(self, inter: disnake.CommandInter) -> None:
        embed = disnake.Embed(
            title="Hi there! This is Tao!",
            description="""
            I hang around, wander and manage this server. I\'m a general-purpose Discord bot.
            I can only do moderation stuff for now, but I think I'm growing up fast and I'll be
            able to do much more pretty soon. You can, for now, ask about me to the
            moderators of the Discord server.
            """,
        ).set_thumbnail(url=self.bot.user.avatar)
        await inter.send(embed=embed, view=HelpView())

    @commands.slash_command(
        name="greet",
        description="Greets a member.",
        options=[
            Option(
                "member",
                "The server member you wish to greet.",
                OptionType.user,
                required=True,
            )
        ],
        dm_permission=False,
    )
    async def _greet(self, inter: disnake.CommandInter, member: disnake.Member):
        await inter.send(f"Greetings, {member.mention}!")

    @commands.slash_command(
        name="info",
        description="Get information about the server.",
        dm_permission=False,
    )
    async def _info(self, inter: disnake.CommandInter):
        embed = (
            disnake.Embed(
                title="Server Information",
            )
            .add_field(name="Server Name", value=inter.guild.name, inline=True)
            .add_field(name="Server ID", value=inter.guild.id, inline=True)
            .add_field(name="Owner", value=inter.guild.owner.mention, inline=True)
            .add_field(
                name="Server Created On",
                value=inter.guild.created_at.strftime("%m/%d/%Y"),
                inline=True,
            )
            .add_field(name="Member Count", value=inter.guild.member_count, inline=True)
            .add_field(
                name="Boost Count",
                value=inter.guild.premium_subscription_count,
                inline=True,
            )
            .set_image(url=inter.guild.icon)
        )
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
