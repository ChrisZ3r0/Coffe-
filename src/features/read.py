#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from features import readcsv as data

def rfidread():
	reader = SimpleMFRC522()
	try:
		id, text = reader.read()
		print(str(id))

		print("Reading id...")

		if(data.checkdata(str(id))):
			print("yey benne van")
			return True
		else:
			print("yeet nincs benne")
			return False

	finally:
        	GPIO.cleanup()
