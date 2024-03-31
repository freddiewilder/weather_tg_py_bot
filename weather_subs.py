import bot
import functions
from time import sleep

SUBSCRIBERS = bot.SUBSCRIBERS

def main():
    try:
        if len(functions.get_users(SUBSCRIBERS)) > 0:
            print("Был запрошен список чатов для рассылки")
            users = functions.get_users(SUBSCRIBERS)
        else:
            print('Нет подписчиков! Прекращаю работу скрипта')
            exit()
    except FileNotFoundError as e:
        print("Нет файла, нет подписчиков!")
        exit()

    tg_bot = bot.bot
    message = functions.get_weather('novosibirsk')

    for i in range(len(users)):
        tg_bot.send_message(users[i], message)
        sleep(2)
        

if __name__ == '__main__':
    main()