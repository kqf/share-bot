import random

from bot.settings import config


async def _forward_to_admins(update, context):
    for admin_id in config.admin_ids:
        await update.message.forward(admin_id)


async def start(update, context):
    await update.message.reply_text(config.message_start)


async def helpme(update, context):
    await update.message.reply_text(config.message_help)


async def forward(update, context):
    await _forward_to_admins(update, context)
    stem = await update.message.text[1:]
    await update.message.reply_text(f"Your next message will be {stem}ed :)")


async def thanks(update, context):
    await _forward_to_admins(update, context)
    await update.message.reply_text(config.message_thanks)
    await update.message.reply_sticker(random.choice(config.thanks_stickers))
