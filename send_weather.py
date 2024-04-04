import bot
import schedule
import os

cur_dir = os.getcwd()
db_file = cur_dir + "/subscribers.txt"
print(db_file)
schedule.every().minute.do(lambda: bot.send_weather(db_file))
print("Запуск скрипта рассылки..")
while True:
    schedule.run_pending()