import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} is now running!")

# Command: Ping
@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

# Run the bot
bot.run(TOKEN)
