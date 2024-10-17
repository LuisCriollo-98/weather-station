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
        role TEXT NOT NULL,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at NULL
    )
'''
#Execute query
cur.execute(users_model)

#close connection
con.close()
