#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import readcsv as data

#print("before reader")


reader = SimpleMFRC522()

#print("after reader")

try:
	id, text = reader.read()
	print(str(id))
#	print(text)

	print("Reading id...")
	#data.load_data()

	if(data.checkdata(str(id))):
		print("yey benne van")
	else:
		print("yeet nincs benne")
        


finally:
        GPIO.cleanup()
