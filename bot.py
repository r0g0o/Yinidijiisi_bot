import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = '1510228902:AAFovuJjk5KnWICSqQxmSl9khxAXHQZhz_E'

def start(update, context):
    update.message.reply_text('Hi!')


def help(update, context):
    update.message.reply_text('Help!')


def echo(update, context):
    """Reemplaza las vocales por la i, ya sea minúscula, mayuscola, con o sin tilde"""

    texto1 = update.message.text

    texto2 = texto1.replace("a", "i").replace("e", "i").replace("o", "i").replace("u", "i")

    texto3 = texto2.replace("A", "I").replace("E", "I").replace("O", "I").replace("U", "I")

    texto4 = texto3.replace("á", "í").replace("é", "í").replace("ó", "í").replace("ú", "í")

    texto5 = texto4.replace("Á", "Í").replace("É", "Í").replace("Ó", "Í").replace("Ú", "Í")
    
    update.message.reply_text(texto5, quote=False)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
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
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://yinidijiisibot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
