"""
Handles commands for the Telegram bot.
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from .. import HISTORY_FILE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    try:
        user_tag = f"<b>@{update.message.from_user.username}</b>"
        welcome_message = f"Привіт, {user_tag}!\nЯ телеграм бот."
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=welcome_message, parse_mode="HTML"
        )
        logging.info("Start command received from %s", user_tag)
    except AttributeError as e:
        logging.error("Error handling /start command: AttributeError: %s", e)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /help command."""
    help_text = (
        "Писати за допомогою @Uni000l'\n"
        "Команди:\n"
        "    /help\n"
        "    /start\n"
        "    /history"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
    logging.info("Help command issued")


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /history command."""
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history_text = f.read()
        if history_text:
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text=history_text
            )
            logging.info("History command executed and history sent")
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text="Історія повідомлень порожня."
            )
            logging.info("History command executed but history is empty")
    except FileNotFoundError:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Історія повідомлень не знайдена."
        )
        logging.error("History file not found")
    except IOError as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Помилка при отриманні історії."
        )
        logging.error("Error handling /history command: IOError: %s", e)
