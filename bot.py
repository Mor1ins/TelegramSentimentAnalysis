import telebot

from Bayes import predict

token = '481955063:AAGwRfDppnW9FH2LeTUKb6OS9RquTbd3ijs'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id,str(predict([message.text])[0][1]))


bot.polling(none_stop=True)