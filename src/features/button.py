import RPi.GPIO as GPIO
import time

def initial():
    GPIO.setmode(GPIO.BOARD)
    #Set Button and LED pins

    global Button1
    global Button2
    global Button3
    global Button4
    global Button5
    global buzzer

    Button1 = 35
    Button2 = 37
    Button3 = 36
    Button4 = 38
    Button5 = 40
    buzzer = 16

    GPIO.setup(Button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Button4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Button5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(buzzer,GPIO.OUT)

    global previous_button_state1
    global previous_button_state2
    global previous_button_state3
    global previous_button_state4
    global previous_button_state5

    # previous_button_state1 = GPIO.input(Button1)
    # previous_button_state2 = GPIO.input(Button2)
    # previous_button_state3 = GPIO.input(Button3)
    # previous_button_state4 = GPIO.input(Button4)
    # previous_button_state5 = GPIO.input(Button5)

def beep():
    GPIO.output(buzzer,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(buzzer,GPIO.LOW)

def buttonpush():
    initial()

    previous_button_state1 = GPIO.input(Button1)
    previous_button_state2 = GPIO.input(Button2)
    previous_button_state3 = GPIO.input(Button3)
    previous_button_state4 = GPIO.input(Button4)
    previous_button_state5 = GPIO.input(Button5)


    try:
        while True:
            time.sleep(0.01)

            button_state1 = GPIO.input(Button1)
            button_state2 = GPIO.input(Button2)
            button_state3 = GPIO.input(Button3)
            button_state4 = GPIO.input(Button4)
            button_state5 = GPIO.input(Button5)

            if button_state1 != previous_button_state1:
                previous_button_state1 = button_state1
                if button_state1 == GPIO.HIGH:
                    print("button1 released")
                    beep()
                    return 1
            if button_state2 != previous_button_state2:
                previous_button_state2 = button_state2
                if button_state2 == GPIO.HIGH:
                    print("button2 released")
                    beep()
                    return 2
            if button_state3 != previous_button_state3:
                previous_button_state3 = button_state3
                if button_state3 == GPIO.HIGH:
                    print("button3 released")
                    beep()
                    return 3
            if button_state4 != previous_button_state4:
                previous_button_state4 = button_state4
                if button_state4 == GPIO.HIGH:
                    print("button4 released")
                    beep()
                    return 4
            if button_state5 != previous_button_state5:
                previous_button_state5 = button_state5
                if button_state5 == GPIO.HIGH:
                    print("button5 released")
                    beep()
                    return 5

    except KeyboardInterrupt:
        GPIO.cleanup()



