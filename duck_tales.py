import telebot
from telebot import types
import schedule, time

bot = telebot.TeleBot() #Token

def duck_story(message):
    duck = 'https://t.me/c/1764712342/9' #Ссылка на пост из Телеграм
    bot.send_message(message.chat.id, duck)
    
schedule.every().day.at("08:00").do(duck_story)

while True: 
    schedule.run_pending()
    time.sleep(1)
    
bot.polling(none_stop=True)
