# bot.py

import os

import disnake
from disnake.ext import commands
from dotenv import load_dotenv
from keep_alive import keep_alive

# Load environment variables.
load_dotenv()
TOKEN = os.getenv("TOKEN")


# Setup bot and its intents.
intents = disnake.Intents.all()
intents.members = True


class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f"{self.user.name} has connected to Discord!")

    async def on_member_join(self, member: disnake.Member):
        print(f"{member} has joined the server.")
        await member.send(f"Welcome, {member.mention}!")
        guild = member.guild
        for channel in guild.channels:
            if channel.name.startswith("Members:"):
                await channel.edit(name=f"Members: {guild.member_count}")
                break


bot = DiscordBot()


# Load cogs / extensions.
for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])


# Run the bot.
if __name__ == "__main__":
    keep_alive()
    bot.run(TOKEN)
