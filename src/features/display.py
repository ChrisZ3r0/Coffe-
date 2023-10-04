#!/usr/bin/python3

from  signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import time
lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM,safe_exit)
signal(SIGHUP,safe_exit)

try:
    message = "Hello2222ysfds222222222dfgdfgfdggfdgdgdfgdfgfd22"
    if (message.size > 16)
    lcd.text(message, 1)
    #lcd.text("Raspberry pnjhghjgiii!!!", 2)
    time.sleep(1.5)

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()