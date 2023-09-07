#Libraries
import RPi.GPIO as GPIO
import buttons
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BOARD)
#Set buzzer - pin 23 as output
buzzer=16
GPIO.setup(buzzer,GPIO.OUT)
#Run forever loop
if buttons.button_callback==True{
    GPIO.output(buzzer,GPIO.HIGH)
    sleep(0.5) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    sleep(0.5)
}