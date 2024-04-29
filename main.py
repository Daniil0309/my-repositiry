import telebot #Библиотека с которой хорошо работает GPT-4
import datetime #модуль который позволяет работать с датой и временем
import time #используется в основном для задержек на 60 сек или 5 сек
import threading #для работы с потоками
import random

bot = telebot.TeleBot('введите токен')


@bot.message_handler(commands=['start'])
def start_message (message): #В message хранится инфа о пользователе
    bot.reply_to(message,'Привет! Я Ваш верный спутник по пути к здоровью и благополучию. Напишите /help для получения справки.')
    reminder_thread = threading.Thread(target=send_reminders,args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['help'])
def help_message(message):
    help_text =  "Я могу выполнить следующие команды:\n" \
                "/start - Начать взаимодействие с ботом\n" \
                "/help - Получить справку о доступных командах\n" \
                "/fact - Получить случайный факт о здоровье\n"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['fact'])
def fact_message (message):
    list = ["Необходимость для жизни: Вода является неотъемлемой частью жизнедеятельности человеческого организма. Она участвует во множестве биохимических процессов, регулирует температуру тела, помогает транспортировать питательные вещества и удалять отходы.",
            "Гидратация: Пить достаточное количество воды важно для поддержания гидратации организма. Недостаток воды может привести к дегидратации, что может проявляться усталостью, головной болью, плохой концентрацией и другими негативными последствиями для здоровья.",
            "Качество воды: Качество питьевой воды играет ключевую роль в обеспечении здоровья человека. Она должна соответствовать определенным стандартам безопасности и чистоты, чтобы избежать риска заражения различными бактериями, вирусами или химическими загрязнителями."]
    random_fact = random.choice(list)
    bot.reply_to(message,f"Лови факт о здоровье - {random_fact}")

def send_reminders(chat_id):
    first_rem = '09:00'
    second_rem = '14:00'
    end_rem = '19:33'
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id,"Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)

