import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

buzzer=16
GPIO.setup(buzzer,GPIO.OUT)

def button_callback(channel):
    print("Button was pushed!")
    print("pin number   " + str(channel))
    GPIO.output(buzzer,GPIO.HIGH)

GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(35,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(36,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(37,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(38,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(40,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
