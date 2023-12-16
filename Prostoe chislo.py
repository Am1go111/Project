elif message.text == "Помощь":
bot.send_message(message.chat.id,
                 'Пока у меня 3 возможности. /start, /button и /aboutyou.Лень рассказывать вам о их возможностях, если хотите сами проверьте')
elif message.text == "Настройки":
bot.send_message(message.chat.id, 'Пока здесь закрыто,возвращайся чуть позже')
elif message.text == "ВК":
bot.send_message(message.chat.id, 'https://vk.com/bukhtoyarov_1')
elif message.text == "Телеграмм":
bot.send_message(message.chat.id, '@Am1go1')
elif message.text == "Инстаграмм":
bot.send_message(message.chat.id, 'bukhtoyarov_1')
elif message.text == "Игры":
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
item1 = types.KeyboardButton("Орел или Решка")
item2 = types.KeyboardButton("Камень,ножницы,бумага")
item3 = types.KeyboardButton("Вернуться назад")
markup.add(item1, item2, item3)
bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
elif message.text == "Вернуться назад":
button(message)
elif message.text == "Орел или Решка":
b = ["Орел", "Решка"]
a = str(random.choice(b))
if a == "Решка":
    bot.send_message(message.chat.id, "Решка")
else:
    bot.send_message(message.chat.id, "Орел")
elif message.text == "Камень,ножницы,бумага":
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.InlineKeyboardButton("Камень")
item2 = types.KeyboardButton("Ножницы")
item3 = types.KeyboardButton("Бумага")
item4 = types.KeyboardButton("Вернуться назад")
markup.add(item1, item2, item3, item4)
bot.send_message(message.chat.id, 'Выберите ваш ход', reply_markup=markup)
elif message.text == "Камень":
b = ["Камень", "Ножницы", "Бумага"]
a = str(random.choice(b))
if a == "Ножницы":
    bot.send_message(message.chat.id, "Блин у меня ножницы,похоже твоя победа")
elif a == "Бумага":
    bot.send_message(message.chat.id,
                     "У меня бумага,главное не расстраивайся ты обязательно выиграешь, но в следущий раз")
else:
    bot.send_message(message.chat.id, "У меня камень,матч закончился в ничью")
elif message.text == "Ножницы":
b = ["Камень", "Ножницы", "Бумага"]
a = str(random.choice(b))
if a == "Бумага":
    bot.send_message(message.chat.id, "Блин у меня бумага,ты выиграл")
elif a == "Камень":
    bot.send_message(message.chat.id, "У меня камень,походу это не твое,ты проиграл")
else:
    bot.send_message(message.chat.id, "У меня ножницы,так и не смогли опрделить победителя,ничья")
elif message.text == "Бумага":
b = ["Камень", "Ножницы", "Бумага"]
a = str(random.choice(b))
if a == "Камень":
    bot.send_message(message.chat.id, "У меня камень,пойду еще потренеруюсь,я проиграл")
elif a == "Ножницы":
    bot.send_message(message.chat.id, "У меня ножницы,знаешь без поражений не бывает побед,ты проиграл")
else:
    bot.send_message(message.chat.id, "У меня бумага,бумага на бумагу равно чему? Правильно НИЧЬЕ")