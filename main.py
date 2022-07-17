# bot.py

import os
import discord
from dotenv import load_dotenv


# Load environment variables.
load_dotenv()
TOKEN = os.getenv('TOKEN')


# Setup bot and its intents.
intents = discord.Intents.default()
intents.members = True

class DiscordBot(commands.Bot):
    def __init__(self):
        super.__init__(
            intents=intents
        )

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

    async def on_member_join(self, member: discord.Member):
        print(f'{member} has joined the server.')
        await member.send(f'Welcome, {member.mention}!')


bot = DiscordBot()


# Load cogs / extensions.
for f in os.listdir("./cogs"):
	if f.endswith(".py")
		client.load_extension("cogs." + f[:-3])


bot.run(TOKEN)
