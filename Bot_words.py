
import telebot
# УДАЛЕНИЕ СЛОВ, СОДЕРЖАЩИХ ФРАЗУ "абв"
bot = telebot.TeleBot(
   'Bot token')  # привязка к боту

# функция удаления


def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(
        m.chat.id, 'Введите текст, из которого будем удалять слова с абв')

# Получение сообщений от пользователя


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, del_some_words(message.text))


bot.polling(none_stop=True, interval=0)  # запуск бота на постоянной основе
