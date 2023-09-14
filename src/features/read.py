#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import readcsv as data

#print("before reader")


reader = SimpleMFRC522()

#print("after reader")

try:
	print("in try")
	id, text = reader.read()
	print("readiinggg")
	print(id)
#	print(text)



	print("Reading id...")
	data.load_data()

        


finally:
        GPIO.cleanup()
