import telebot
import os

bot = telebot.TeleBot("7998495021:AAEMcQyjB3dzCK1_2a3xqosDgabeq4nrFd8")

@bot.message_handler()
def send_welcome(message):
    try:
        if os.path.getsize() < 10:
            

bot.infinity_polling()