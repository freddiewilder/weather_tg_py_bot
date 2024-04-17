import functions as lib

API_KEY = lib.API_KEY
bot = lib.BOT
SUBSCRIBERS = 'subscribers.txt'

@bot.message_handler(commands=['start', 'help', 'sub', 'unsub', 'joke'])
def send_welcome(message):
    match message.text:
        case '/sub':
            subscribe(message)
        case '/unsub':
            unsub(message)
        case '/joke' : 
            bot.reply_to(message, lib.get_joke())
        case _:
            bot.reply_to(message, "Привет! Напиши /sub чтобы получать прогноз погоды Новосибирска ежедневно утром и вечером!\n"
                            f"Так же ты можешь написать название любого города чтобы получить прогноз погоды на данный момент!")

@bot.message_handler(content_types=["text"])
def weather(message):
    try:
        bot.send_message(message.chat.id, lib.gis.get_weather(message.text, lib.GISMETEO_API))
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
    print("Запускаю бота..")
    bot.infinity_polling()

if __name__ == '__main__':
    main()