import telebot 
import random

TOKEN = '7650477410:AAE51zvutL4PojdI79mugPZqUEX6hiGnmBQ'
bot = telebot.TeleBot(TOKEN)

# Список комплиментов (храним в памяти)
compliments = [
    "Ты замечательный!",
    "У тебя отличное чувство юмора!",
    "Ты приносишь радость людям!",
    "Ты невероятно умный!",
    "Сегодня твой день!"
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=["compliment"])
def send_compliment(message):
    bot.send_message(message.chat.id, random.choice(compliments))

bot.polling()