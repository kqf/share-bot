
def start(update, context):
    update.message.reply_text('Hi!')


def helpme(update, context):
    update.message.reply_text('Help!')


def echo(update, context):
    update.message.reply_text(update.message.text)
