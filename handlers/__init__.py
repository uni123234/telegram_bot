"""
This module imports all handlers for the Telegram bot.
"""

from .error import error_handler
from .commands import start, help_command, history
from .messages import unknown_command, unsupported_message, non_text_message
from . import bot
