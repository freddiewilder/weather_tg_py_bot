import requests
from dotenv import load_dotenv
from os import getenv
from datetime import time, datetime
from time import sleep

load_dotenv()
API_KEY = getenv('API_KEY')
SUBSCRIBERS = 'subscribers.txt'

def get_users(dump_path=SUBSCRIBERS):
    with open(file=dump_path, mode="r") as file:
        users_id = file.readlines()
    users_id = [n.rstrip() for n in users_id]
    return(users_id)

def save_id(user_id, dump_path=SUBSCRIBERS):

    uid_str=str(user_id)
    
    try:

        with open (dump_path, 'r') as file:
            user = file.readlines()

        user = [n.strip() for n in user]

        try:
            if user[user.index(uid_str)] == uid_str:
                print('Got ya!')
                return False

        except ValueError as e:

            with open (dump_path, 'a') as file:
                file.write(uid_str + "\n")
            with open (dump_path, 'r') as file:
                user = file.readlines()
            user = [n.strip() for n in user]

            if user[user.index(uid_str)] == uid_str:
                print('New value Exception: Added!')
                return True

            else:
                print('Между входным и выходным значением несовпадение. Неправильная запись!')
                return False
            
    except FileNotFoundError:
        with open (dump_path, 'w') as file:
            file.write(uid_str + '\n')
        print("FNF: Added!")
        return True

def del_id(target_id = None, dump_path = SUBSCRIBERS):
    users = get_users()
    try:
        users.pop(users.index(str(target_id)))
        if len(users) == 0:
            print("Flag 1")
            with open(SUBSCRIBERS, "w") as file:
                file.write("")
            return True
        else:
            print('Flag 2')
            if len(users) > 0:
                print ("Flag 2.1")
                with open(SUBSCRIBERS, "w") as file:
                    for i in range(len(users)):
                        file.write(users[i] + "\n")
            else:
                print ("Flag 2.2")
                with open(SUBSCRIBERS, 'w') as file:
                    file.write("")
            return True
    except ValueError as e:
        print (e)
        print("Del_id error")
        return False


def get_weather(city = 'Moscow', API_KEY = API_KEY):

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
        )
        data = r.json()
        
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]         #ощущается
        humidity = data["main"]["humidity"]             #влажность
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        pressure = data["main"]["pressure"]             #давление
        wind_speed = data["wind"]["speed"]
        weather_description = data["weather"][0]["description"]
        sunrise_timestamp = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M')
        sunset_timestamp = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M')
        length_of_the_day = datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.fromtimestamp(data["sys"]["sunrise"])
        day_lenght = time.fromisoformat(str(length_of_the_day)).strftime('%H часов %M минут(у)')

        return (f"В городе сейчас {weather_description}\n"
                f"Температура {temp}C°. Ожидаемый минимум и максимум на сегодня: {temp_min}C°/{temp_max}C°\n"
                f"Ощущается как {feels_like}C°\n"
                f"Влажность {humidity}%. Давление {pressure} мм.рт.ст. Скорость ветра {wind_speed}м/с\n"
                f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {day_lenght}\n"
                f"***Хорошего дня!***")

    except Exception as e:
        print(e)
        return ("Ошибка в названии города! ")



    

def main():
   return 0

if __name__ == '__main__':
    main()