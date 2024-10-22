'''
Dev: Luis C.
Script description: weather-station Database
Engine: SQLite3
Date: 09-09-2024

'''
#Import database engine package
import sqlite3

#Create weather-stations database
con = sqlite3.connect('weather_station.db')

#Create cursor
cur=con.cursor()

#Users model
users_model= '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        role INTEGER NOT NULL DEFAULT 1,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at NULL
    )
'''
#Sensor model
sensor_model= '''
    CREATE TABLE IF NOT EXISTS sensors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        model TEXT NOT NULL,
        description TEXT NOT NULL,
        url_datasheet TEXT NULL,
        url_image TEXT NULL,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at NULL
    )
'''
#Execute query
cur.execute(users_model)
cur.execute(sensor_model)

#close connection
#con.close()
