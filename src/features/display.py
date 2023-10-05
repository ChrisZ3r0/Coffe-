#!/usr/bin/python3

from  signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import time
from features import readcsv as text
lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM,safe_exit)
signal(SIGHUP,safe_exit)

try:
     
    # if (kave.size > 16)
    lcd.text(kave, 1)
    #lcd.text("Raspberry pnjhghjgiii!!!", 2)
    time.sleep(4.5)

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()