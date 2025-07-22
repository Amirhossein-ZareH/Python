import telebot
import os

bot = telebot.TeleBot("7998495021:AAEMcQyjB3dzCK1_2a3xqosDgabeq4nrFd8")

# @bot.message_handler()
# def send_welcome(message):
#     if os.path.getsize('test.txt') < 10:
#         with open('test.txt' , 'a') as file:
#             file.write(f"hello {message.from_user.first_name} {message.from_user.last_name}\n")    
#     with open('test.txt', 'rb') as file:
#         bot.send_document(message.chat.id , file)
    
@bot.message_handler(func=lambda message: True)
def send_image(message):
    with open("test.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo)


bot.infinity_polling()