import random

from bot.settings import config


def start(update, context):
    update.message.reply_text(config.message_start)


def helpme(update, context):
    update.message.reply_text(config.message_help)


def thanks(update, context):
    for admin_id in config.admin_ids:
        update.message.forward(admin_id)

    update.message.reply_text(config.message_thanks)
    update.message.reply_sticker(random.choice(config.thanks_stickers))
