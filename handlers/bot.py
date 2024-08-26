"""
This module contains the bot setup and handlers for various commands and message types.
"""

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from . import (
    error_handler,
    start,
    help_command,
    history,
    unknown_command,
    unsupported_message,
    non_text_message,
)
from .utils import save_message_to_history
from .. import BOT_TOKEN


def create_application() -> Application:
    """Create and configure the Telegram bot application."""
    application = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help_command)
    history_handler = CommandHandler("history", history)

    # Message handlers
    message_handler = MessageHandler(
        filters.TEXT & ~filters.COMMAND, save_message_to_history
    )  # Exclude commands
    unknown_command_handler = MessageHandler(filters.COMMAND, unknown_command)

    # Handle unsupported message types
    unsupported_message_handler = MessageHandler(
        filters.AUDIO
        | filters.DOCUMENT
        | filters.PHOTO
        | filters.STICKER
        | filters.VIDEO
        | filters.VOICE
        | filters.VIDEO_NOTE
        | filters.CONTACT
        | filters.LOCATION
        | filters.VENUE
        | filters.GAME
        | filters.INVOICE
        | filters.SUCCESSFUL_PAYMENT
        | filters.ANIMATION
        | filters.POLL
        | filters.DICE,
        unsupported_message,
    )

    # Handle non-text messages
    non_text_message_handler = MessageHandler(filters.TEXT, non_text_message)

    # Add handlers to the application
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(history_handler)
    application.add_handler(message_handler)
    application.add_handler(unknown_command_handler)
    application.add_handler(unsupported_message_handler)
    application.add_handler(non_text_message_handler)

    # Add error handler
    application.add_error_handler(error_handler)

    return application
