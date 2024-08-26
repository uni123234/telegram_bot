"""
Handles non-command messages for the Telegram bot.
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles unknown commands."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Не розумію команду. Спробуйте ще раз.",
    )
    logging.warning("Unknown command received")


async def unsupported_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles unsupported message types."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Вибачте, не підтримую надсилання таких повідомлень.",
        parse_mode="HTML",
    )
    logging.warning("Unsupported message type received")


async def non_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles non-text messages."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, this bot only accepts text messages.",
    )
    logging.warning("Non-text message received")
