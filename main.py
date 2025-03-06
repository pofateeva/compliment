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
    bot.send_message(message.chat.id, 'Привет! Если хочешь получить комплимент напиши /compliment, если хочешь добавить новый комплимент, напиши /add_compliment!')

@bot.message_handler(commands=["compliment"])
def send_compliment(message):
    bot.send_message(message.chat.id, random.choice(compliments))

@bot.message_handler(commands=["add_compliment"])
def add_compliment(message):
    bot.send_message(message.chat.id, "Напиши новый комплимент, который хочешь добавить.")
    bot.register_next_step_handler(message, save_new_compliment)

def save_new_compliment(message):
        compliments.append(message.text)
        bot.send_message(message.chat.id, "Комплимент добавлен! ❤️")

bot.polling()