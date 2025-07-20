import telebot
import os

bot = telebot.TeleBot("7998495021:AAEMcQyjB3dzCK1_2a3xqosDgabeq4nrFd8")

@bot.message_handler()
def send_welcome(message):
    if os.path.getsize('test.txt') < 10:
        with open('test.txt' , 'a') as file:
            file.write('Hello')       
    with open('test.txt', 'rb') as file:
        bot.send_document(message.chat.id , file)

bot.infinity_polling()