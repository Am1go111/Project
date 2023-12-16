import telebot
from telebot import types
token = "5674083733:AAHIhp04CjEmsmQd7x_s8Y-3tlwecub1Ymc"
bot= telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Привет! Здесь ты можешь приобрести подписку в самый информативный чат о хрен знает о чем")
    bot.send_message(message.chat.id,"Чтобы оплатить нажмите кнопку тарифы и следуйте указаниям")
    bot.send_message(message.chat.id,"* Приём оплат произовдить лучше в долларах,они мне нужнее")
    button(message)
@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    item1 = types.KeyboardButton("Тарифы")
    item2 = types.KeyboardButton("Подписка")
    item3 = types.KeyboardButton("Подробнее о чате")
    item4 = types.KeyboardButton("Политика конфиденциальности")
    item5 = types.KeyboardButton("оферта")
    item6 = types.KeyboardButton("Обратная связь")
    markup.add(item1,item2,item3,item4,item5,item6)
    bot.send_message(message.chat.id,"Выберите что вам надо", reply_markup = markup)
@bot.message_handler(content_types="text")
def otvet(message):
    if message.text == "Тарифы":
         bot.send_message(message.chat.id,"Советую не покупать пока что воздух")
    elif message.text == "Подписка":
        bot.send_message(message.chat.id,"Мы не даем подписки на воздух")
    elif message.text == "Подробнее о чате":
        bot.send_message(message.chat.id,"Тыкайте Лизу,что бы она дала информацию Арсению,а пока тут тоже воздух")
    elif message.text == "Политика конфиденциальности":
        bot.send_message(message.chat.id,"Наша политика:делать деньги пока ты спишь")
    elif message.text == "оферта":
        bot.send_message(message.chat.id,"'Шум сверчков'")
    elif message.text == "Обратная связь":
        bot.send_message(message.chat.id,"Ее нет,так же как и идей")
    else:
        button(message)


bot.infinity_polling()

