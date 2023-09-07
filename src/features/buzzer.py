import RPi.GPIO as GPIO
import buttons as bt
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BOARD)
buzzer=16
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,GPIO.HIGH)
sleep(0.5) # Delay in seconds
GPIO.output(buzzer,GPIO.LOW)
sleep(0.5)
if (bt.pressed):
    GPIO.output(buzzer,GPIO.HIGH)
    sleep(0.5) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    sleep(0.5)
