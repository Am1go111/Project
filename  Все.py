from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import logging

logging.basicConfig(format='%(levelname) s - %(message)s',level = logging.DEBUG)
logger = logging.getLogger(__name__)

updater = None
token = "5687598288:AAHbZJXol0PhCatdzTnDkZ49utiOvrtUkSs"

def start_bot():
    global updater
    updater = Updater(
        token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('aboutyou', aboutyou))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.text, repeater))
    dispatcher.add_handler(CommandHandler('echo', echo))
    dispatcher.add_handler(CommandHandler('image', image, filters=Filters.user(username="@Am1go1")))
    updater.start_polling()
    updater.idle()

def start(update, context):
    s = "Welcome I Am The Mr_Amigo Bot! Your life has now changed forever."
    update.message.reply_text(s)

def aboutyou(update,context):
    s = "Я бот который был создан Арсением, сейчас я мало чего могу,но это начало. Знаете все начиналось с малого. Вы всегда можете следить за функционалом с помощью команды /help"
    update.message.reply_text(s)

def help(update,context):
    s = "Пока у меня 2 возможности. /start и /aboutyou.Лень рассказывать вам о их возможностях, если хотите сами проверьте."
    update.message.reply_text(s)

def repeater(update, context):
    if context.user_data[echo]:
        update.message.reply_text(update.message.text)

def echo(update, context):
    command = context.args[0].lower()
    if("on" == command):
        context.user_data[echo] = True
        update.message.reply_text("Repeater Started")
    elif("off" == command):
        context.user_data[echo] = False
        update.message.reply_text("Repeater Stopped")


def image(update, context):
    terms = ",".join(context.args).lower()
    update.message.reply_text(f"Getting Image For Terms: {terms}")
    command = context.args[0].lower()
    if("on" == command):
        context.user_data[echo] = True
        update.message.reply_text("Repeater Started")
    elif("off" == command):
        context.user_data[echo] = False
        update.message.reply_text("Repeater Stopped")





start_bot()