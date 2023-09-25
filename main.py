import telebot

bot = telebot.TeleBot('6543463555:AAEtz4zegf0TK6oJluePPMG9KJqitmuJtvo')

# список для хранения каналов
channels = ['@polezpolez']


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Приветствую {message.from_user.first_name}  {message.from_user.last_name} \nОтправьте вашу анкету одним следующим сообщением \nимя фамилия возраст специальность '
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message('@polezpolez', 'hello')

@bot.message_handler(func=lambda message:True)
def handle_message(message):
    user_message = message.text.split()
    for channel in channels:
        bot.send_message(channel, f'Имя = {user_message[0]} \nФамилия =  {user_message[1]} \nИмя = {user_message[2]} \nИмя = {user_message[3]} \n')
    bot.send_message(message.chat.id, 'Ваша анкета отправлена по группам', parse_mode='html')

bot.polling(none_stop=True)