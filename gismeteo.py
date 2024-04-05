import requests
from geopy.geocoders import Nominatim as geo
from datetime import datetime

def get_weather(city: str, API_TOKEN :str) -> str: 

    try:
        locator = geo(user_agent="Mozilla/5.0 (Windows; U; Windows NT 6.3; x64; en-US) Gecko/20130401 Firefox/69.2")
        location = locator.geocode(city)
    except Exception as e:
        print(e)
        exit()

    host = "https://api.gismeteo.net"
    get_current = "/v3/weather/current"
    payload = {
        "latitude" : location.latitude,
        "longitude" : location.longitude
    }

    headers = {
        'X-Gismeteo-Token' : API_TOKEN
    }

    try:
        req = requests.get(f"{host}{get_current}", params = payload, headers = headers)
    except Exception as e:
        print(e)
        exit()

    res = req.json() 

    nameP = res['data']['city']['nameP']
    description = res['data']['description']
    humidity = res['data']['humidity']['percent']    #влажность
    precipitation_amount = res['data']['precipitation']['amount'] #количество осадков в мм
    precipitation_type = res['data']['precipitation']['type'] #тип осадков 0 - Нет осадков; 1 - Дождь; 2 - Снег; 3 - Смешанные
    precipitation_intens = res['data']['precipitation']['intensity'] # интенсивность осадков по возрастающей от 0 до 3
    pressure = res['data']['pressure']['mm_hg_atm'] #давление в мм.рт.ст
    air_temp = res['data']['temperature']['air']['C']
    comfort_temp = res['data']['temperature']['comfort']['C']
    water_temp = res['data']['temperature']['water']['C']
    wind_speed = res['data']['wind']['speed']['m_s']
    sunrise = datetime.strptime(res['data']['astro']['sun']['sunrise'][:-6], '%Y-%m-%dT%H:%M:%S')
    sunset = datetime.strptime(res['data']['astro']['sun']['sunset'][:-6], '%Y-%m-%dT%H:%M:%S')
    next_full_moon = datetime.strptime(res['data']['astro']['moon']['next_full'][:-6], '%Y-%m-%dT%H:%M:%S')

    return (
        f"Погода {nameP}\n"
        f"{description}. Температура воздуха: {air_temp}°C. По ощущениям: {comfort_temp}°C\n"
        f"Влажность: {humidity}%. Давление: {pressure} мм.рт.ст\n"
        f"Скорость ветра: {wind_speed} м/с. Количество осадков: {precipitation_amount} мм\n"
        f"Восход: {sunrise.strftime("%H:%M")}\n"
        f"Закат: {sunset.strftime("%H:%M")}\n"
        f"Ближайшее полнолуние: {next_full_moon.strftime("%d.%m")}\n"
        f"Поставщик метеоданных : GISMETEO"
    )  