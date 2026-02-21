import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

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

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# ----------------------------
# Events
# ----------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Bot is online!")

# ----------------------------
# Load Cogs
# ----------------------------
for root, dirs, files in os.walk("./cogs"):
    for file in files:
        if file.endswith(".py"):
            cog_path = os.path.join(root, file)
            module = cog_path.replace("./", "").replace("/", ".").replace("\\", ".")[:-3]
            try:
                bot.load_extension(module)
                print(f"Loaded extension: {module}")
            except Exception as e:
                print(f"Failed to load {module}: {e}")

# ----------------------------
# Run Bot
# ----------------------------
if __name__ == "__main__":
    bot.run(BOT_TOKEN)
