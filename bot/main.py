import logging


from telegram.ext import Application, CommandHandler, MessageHandler, Filters

from bot.commands import start, helpme, thanks, forward
from bot.settings import config


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    app = Application.builder().token(config.token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", helpme))
    app.add_handler(CommandHandler("copyright", forward))
    app.add_handler(CommandHandler("forward", forward))
    app.add_handler(MessageHandler(~Filters.command, thanks))

    # No webhook -- run in the debug mode
    if config.webhook is None:
        app.run_polling()
        app.idle()
        return

    app.run_polling(
        listen="0.0.0.0",
        port=config.port,
        url_path=config.token,
        webhook_url=config.webhook,
    )


if __name__ == "__main__":
    main()
