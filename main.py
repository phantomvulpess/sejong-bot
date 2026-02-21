import os
from dotenv import load_dotenv
import discord
from discord.ext import bridge

# ----------------------------
# Load environment variables
# ----------------------------

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set")

# ----------------------------
# Bot Setup
# ----------------------------
intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages

bot = bridge.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# ----------------------------
# Events
# ----------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.sync_commands()
        print(f"Slash commands synced: {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync slash commands: {e}")

    print("Bot is online!")

# ----------------------------
# Load Cogs
# ----------------------------

extensions = [
    "cogs.dictionary.cog",
    "cogs.hanja.cog",
    "cogs.support",
]

for ext in extensions:
    try:
        bot.load_extension(ext)
        print(f"Loaded extension: {ext}")
    except Exception as e:
        print(f"Failed to load {ext}: {e}")

# ----------------------------
# Run Bot
# ----------------------------
if __name__ == "__main__":
    bot.run(BOT_TOKEN)
