#Libraries
import RPi.GPIO as GPIO
from time import sleep
#Set warnings off (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Set Button and LED pins
Button = 38
Buzzer = 16
#Setup Button and LED
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Buzzer,GPIO.OUT)
#flag = 0

while True:
    button_state = GPIO.input(Button)
    print(button_state)
    if button_state == 0:
        GPIO.output(Buzzer,GPIO.HIGH)
    else:
        GPIO.output(Buzzer,GPIO.LOW)
    sleep(1)
    '''
    if button_state==0:
        sleep(0.5)
        if flag==0:
            flag=1
        else:
            flag=0
    if flag==1:
        GPIO.output(LED,GPIO.HIGH)
    else:
        GPIO.output(LED,GPIO.LOW)  
    '''
