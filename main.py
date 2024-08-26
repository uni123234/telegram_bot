"""
Main module to run the Telegram bot application.
"""

import logging
from telegram_bot.handlers.bot import create_application
from . import LOG_DIR

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler(f"{LOG_DIR}/bot.log"), logging.StreamHandler()],
)


def main() -> None:
    """Main function to run the bot."""
    application = create_application()
    logging.info("Starting the bot...")
    application.run_polling()


if __name__ == "__main__":
    main()
