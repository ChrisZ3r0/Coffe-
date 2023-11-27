#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
#from features import readcsv as data
from . import readdata as data


def rfidread():
	reader = SimpleMFRC522()
	try:
		id, text = reader.read()
		#print(str(id))

		if(data.checkcardid(str(id))):
			#print("yey benne van")
			return True,str(id)
		else:
			#print("yeet nincs benne")
			return False,str(id)
		


	finally:
        	GPIO.cleanup()
