import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = '1510228902:AAFovuJjk5KnWICSqQxmSl9khxAXHQZhz_E'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""

    texto1 = update.message.text

    texto2 = texto1.replace("a", "i")
    texto3 = texto2.replace("e", "i")
    texto4 = texto3.replace("o", "i")
    texto5 = texto4.replace("u", "i")

    texto6 = texto5.replace("A", "I")
    texto7 = texto6.replace("E", "I")
    texto8 = texto7.replace("O", "I")
    texto9 = texto8.replace("U", "I")

    texto10 = texto9.replace("á", "í")
    texto11 = texto10.replace("é", "í")
    texto12 = texto11.replace("ó", "í")
    texto13 = texto12.replace("ú", "í")

    texto14 = texto13.replace("Á", "Í")
    texto15 = texto14.replace("É", "Í")
    texto16 = texto15.replace("Ó", "Í")
    texto17 = texto16.replace("Ú", "Í")

    update.message.reply_text(texto17, quote=False)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    '''
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    '''
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    print('Ejecutandose')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()