import serial;
import time;
import mysql.connector
from datetime import datetime

database = mysql.connector.connect(
    host = "127.0.0.2",
    user = "root",
    password = "583103",
    database = "arduino",    
)

arduino = serial.Serial(port="COM18",baudrate=9600,timeout=1)
time.sleep(2)
arduino.reset_input_buffer()
while True:
    raw_data=arduino.readline()
    decoded_str = raw_data.decode('utf-8').strip()
    temp_var = decoded_str.split("x")
    temprature = int(temp_var[0])
    humidity = int(temp_var[1])
    now = datetime.now()
    database.cursor().execute("INSERT INTO data (time,temp,humid) VALUES (%s,%s,%s)",(now,temprature,humidity))
    database.commit()
        
        