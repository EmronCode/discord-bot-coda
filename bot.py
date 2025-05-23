import discord
from discord.ext import commands
import asyncio
import os

# === CONFIG ===
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def main():
    # Load the TicTacToe feature
    await bot.load_extension("features.tictactoe.feature")
    await bot.start(TOKEN)

asyncio.run(main())