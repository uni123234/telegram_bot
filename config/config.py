"""
Configuration file for the Telegram bot.

This file reads the bot token and the path to the history file from environment variables.
"""

import os

# Fetch the Telegram bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Path to the history file
HISTORY_FILE: str = os.getenv("HISTORY_FILE", "history.txt")

# Directory for log files
LOG_DIR: str = os.getenv("LOG_DIR", "logs")

# Create logs directory if it does not exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Ensure the bot token is set
if not BOT_TOKEN:
    raise ValueError("Bot token must be set in the environment variables.")
