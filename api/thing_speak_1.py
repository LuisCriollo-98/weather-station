import time;
import random;
import requests;

THINGSSPEAK_API_KEY = "LJC6LEE9PBGUJE9R"
THINGSSPEAK_CHANNEL_ID= "2739531"

def send_data():
    last_temp = 0
    last_hum = 0

    while True:
        temperature = random.uniform(-10,100)
        humidity = random.uniform(0,100)

        url = f"https://api.thingspeak.com/update?api_key={THINGSSPEAK_API_KEY}"

        payload = {
            'field1': {temperature},
            'field2': {humidity}
        }
        response = requests.get(url, data=payload) 
        if temperature != last_temp or humidity != last_hum:
            if response.status_code == 200:
                print(f"Datos enviados a ThingSpeak: Temperatura: {temperature:.2f}°C, Humedad: {humidity:.2f}%")
                last_temp = temperature
                last_hum = humidity
            else:
                print(f"Datos no enviados : {response.status_code}")
        time.sleep(3)
send_data()