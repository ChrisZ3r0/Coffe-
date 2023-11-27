#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
#from features import readcsv as data
from . import readdata as data
global checkstatus
checkstatus=True

def rfidread():
	global checkstatus
	reader = SimpleMFRC522()
	try:
		id, text = reader.read()
		#print(str(id))

		#print("Reading id...")

		if get_check():

			if(data.checkcardid(str(id))):
				#print("yey benne van")
				return True,str(id)
			else:
				#print("yeet nincs benne")
				return False,str(0)
		else:
			return id
			read_check_reset()


	finally:
        	GPIO.cleanup()

def read_id_for_server():
	reader = SimpleMFRC522()
	try:
		id, text = reader.read()

		return id
	finally:
    		GPIO.cleanup()

def get_check():
	global checkstatus
	print(checkstatus)
	if checkstatus:
		return True
	else:
		return False

def set_check():
	global checkstatus
	checkstatus=False
	print(checkstatus)


def read_check_reset():
	global checkstatus
	checkstatus = True
