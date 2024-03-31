import functions as lib

API_KEY = lib.API_KEY
bot = lib.BOT
SUBSCRIBERS = 'subscribers.txt'

def send_weather(dump_path=SUBSCRIBERS):

    try:
        users = lib.get_users()
        weather = lib.get_weather()

        for n in users:
            print(n, weather)
            bot.send_message(chat_id = n, text = weather)
            lib.sleep(5)
    except Exception as e:
        print(e)
    return 0

@bot.message_handler(commands=['start', 'help', 'sub', 'unsub'])
def send_welcome(message):
    match message.text:
        case '/sub':
            subscribe(message)
        case '/unsub':
            unsub(message)
        case _:
            bot.reply_to(message, "Привет! Напиши /sub чтобы получать прогноз погоды Новосибирска ежедневно утром и вечером!\n"
                            f"Так же ты можешь написать название любого города чтобы получить прогноз погоды на данный момент!")

@bot.message_handler(content_types=["text"])
def weather(message):
    try:
        bot.send_message(message.chat.id, lib.get_weather(message.text))
    except Exception as e:
        print(e)
        bot.reply_to(message, "Нет такого города :с")

def subscribe(message):
    if lib.save_id(message.chat.id):
        bot.reply_to(message, "Теперь ты подписан!")
    else:
        bot.reply_to(message, "Ты уже подписан!")

def unsub(message):
    if lib.del_id(message.chat.id):
        bot.reply_to(message, "Теперь ты отписан :с")
    else:
        bot.reply_to(message, "Сперва подпишись чтобы отписываться!")

def main():
    bot.infinity_polling()
    

if __name__ == '__main__':
    main()