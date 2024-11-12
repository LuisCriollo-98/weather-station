import time;
import random;
import requests;

THINGSSPEAK_API_KEY = "FQGL7Y9UI5T3KNSF"
THINGSSPEAK_CHANNEL_ID= "2739663"

def send_data():
    while True:
        consumo_nevera = random.uniform(100,400)
        consumo_lavadora = random.uniform(400,1500)
        consumo_ducha= random.uniform(3000,5500)
        consumo_computador= random.uniform(100,450)

        url = f"https://api.thingspeak.com/update?api_key={THINGSSPEAK_API_KEY}"

        payload = {
            'field1' : {consumo_nevera},
            'field2' : {consumo_lavadora},
            'field3' : {consumo_ducha},
            'field4' : {consumo_computador}
        }

        response = requests.get(url, data=payload)

        if response.status_code == 200:
            print(f"\nEnviando datos a ThingSpeak:\n"
                  f"Nevera: {consumo_nevera:.2f} W\n"
                  f"Lavadora: {consumo_lavadora:.2f} W\n"
                  f"Ducha: {consumo_ducha:.2f} W\n"
                  f"Computador: {consumo_computador:.2f} W\n"
                  )
        else: 
            print(f"Error al enviar los datos: {response.status_code}")
        time.sleep(10)
send_data()