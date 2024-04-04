import functions as lib
import schedule
import os

db_file = os.path.abspath('subscribers.txt')
print(db_file)
lib.send_weather(db_file)