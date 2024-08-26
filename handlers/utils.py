"""
Utility functions for the Telegram bot.

This module contains helper functions used by the bot, such as saving messages to the history file.
"""

import logging
from .. import HISTORY_FILE

# Configure logging
logging.basicConfig(
    filename='logs/bot.log',  # Log file path
    level=logging.INFO,       # Minimum log level to capture
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def save_message_to_history(update):
    """Save text messages to the history file."""
    if update.message.text:
        try:
            with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
                f.write(update.message.text + '\n')
            # Log success
            logging.info("Message saved to history: %s", update.message.text)
        except IOError as e:
            # Log the error if file operation fails
            logging.error("Failed to save message to history: %s", e)
