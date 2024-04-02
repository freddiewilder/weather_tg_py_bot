import bot
import schedule


schedule.every().minute.do(lambda: bot.send_weather('subscribers.txt'))
print("Запуск скрипта рассылки..")
while True:
    schedule.run_pending()