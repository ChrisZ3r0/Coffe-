#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import readcsv as data

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)



        print("Reading id...")
        data.load_data()

        


finally:
        GPIO.cleanup()
