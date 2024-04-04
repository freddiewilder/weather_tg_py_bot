import bot
import schedule
import os

db_file = os.path.abspath('subscribers.txt')
print(db_file)
schedule.every().minute.do(lambda: bot.send_weather(db_file))
print("Запуск скрипта рассылки..")
while True:
    schedule.run_pending()