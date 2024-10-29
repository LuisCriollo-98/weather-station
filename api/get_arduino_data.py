'''
Script description
Get temperature and humidity from DTH11 since Arduino.
Devolper: Luis C.
'''
#Import Libraries
import serial
import serial.tools.list_ports ##Detectar los puertos abiertos
import time
from detect_arduino_port import p

#Arduino port
arduino_port = p
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    time=1
)

time.sleep(1) #Delay

while True:
    #data = service.readline.decode('utf-8').strip()
    data = service.readline.decode('utf-8').rstrip()

    if data:
        temp,hum = data.split(",")

        print(f"Temperature: {temp} °C")
        print(f"Humidity: {hum}%")

        # 1. Create new model data called test_data
        # Fields: id, temp, hum, created_at
        # 2. Create a method tio insert data into test_data
        # 3. Update method: Insert data when detect changes in temp or hum

    time.sleep(1)