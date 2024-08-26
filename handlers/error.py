"""
Handles errors for the Telegram bot.
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from .. import LOG_DIR

# Configure logging
logging.basicConfig(
    filename=f"{LOG_DIR}/bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors and send a message to the chat."""
    logging.error("An error occurred", exc_info=context.error)
    if update.effective_chat:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Виникла помилка при обробці вашого запиту. Будь ласка, спробуйте ще раз пізніше.",
        )
