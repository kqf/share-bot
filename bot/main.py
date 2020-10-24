import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot.commands import start, helpme, thanks, forward
from bot.settings import config


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    updater = Updater(config.token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helpme))
    dp.add_handler(CommandHandler("copyright", forward))
    dp.add_handler(CommandHandler("forward", forward))
    dp.add_handler(MessageHandler(~Filters.command, thanks))

    # No webhook -- run in the debug mode
    if config.webhook is None:
        updater.start_polling()
        updater.idle()
        return

    updater.start_webhook(
        listen="0.0.0.0",
        port=config.port,
        url_path=config.token
    )
    updater.bot.set_webhook(config.webhook)
    updater.idle()


if __name__ == '__main__':
    main()
