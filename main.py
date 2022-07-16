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

bot = commands.Bot(intents=intents)


# Event handlers.
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    print(f"{member} has joined the server.")
    await member.send(f"Welcome! {member.mention}")


# Load cogs / extensions.
for f in os.listdir("./cogs"):
	if f.endswith(".py")
		client.load_extension("cogs." + f[:-3])


bot.run(TOKEN)
