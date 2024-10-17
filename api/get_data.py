'''
Script description
Get temperature and humidity from DTH11 since Arduino.
Devolper: Luis C.
'''
#Import Libraries
import serial
import time

#Arduino port

arduino_port = 'COM7'
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
    time.sleep(1)