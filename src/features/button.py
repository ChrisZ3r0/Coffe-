import RPi.GPIO as GPIO
import time
from features import beep
import features.display as dp

def initial():
    GPIO.setmode(GPIO.BOARD)

    global Button1
    global Button2
    global Button3
    global Button4
    global Button5
    global exitbutton

    Button1 = 35
    Button2 = 37
    Button3 = 36
    Button4 = 38
    Button5 = 40
    exitbutton = 33


    GPIO.setup(Button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Button4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Button5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(exitbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)

    global previous_button_state1
    global previous_button_state2
    global previous_button_state3
    global previous_button_state4
    global previous_button_state5
    global previous_exit_button_state

def buttonpush():
    initial()

    exit = False

    previous_button_state1 = GPIO.input(Button1)
    previous_button_state2 = GPIO.input(Button2)
    previous_button_state3 = GPIO.input(Button3)
    previous_button_state4 = GPIO.input(Button4)
    previous_button_state5 = GPIO.input(Button5)
    previous_exit_button_state = GPIO.input(exitbutton)
    

    try:
        while not exit:
            time.sleep(0.01)

            button_state1 = GPIO.input(Button1)
            button_state2 = GPIO.input(Button2)
            button_state3 = GPIO.input(Button3)
            button_state4 = GPIO.input(Button4)
            button_state5 = GPIO.input(Button5)
            exitbutton_state = GPIO.input(exitbutton)

            if button_state1 != previous_button_state1:
                previous_button_state1 = button_state1
                if button_state1 == GPIO.HIGH:
                    print("button1 released")
                    dp.buttonpushsignal()
                    beep.standardSound()
                    return 1
            if button_state2 != previous_button_state2:
                previous_button_state2 = button_state2
                if button_state2 == GPIO.HIGH:
                    print("button2 released")
                    beep.standardSound()
                    dp.buttonpushsignal()
                    return 2
            if button_state3 != previous_button_state3:
                previous_button_state3 = button_state3
                if button_state3 == GPIO.HIGH:
                    print("button3 released")
                    beep.standardSound()
                    dp.buttonpushsignal()
                    return 3
            if button_state4 != previous_button_state4:
                previous_button_state4 = button_state4
                if button_state4 == GPIO.HIGH:
                    print("button4 released")
                    beep.standardSound()
                    dp.buttonpushsignal()
                    return 4
            if button_state5 != previous_button_state5:
                previous_button_state5 = button_state5
                if button_state5 == GPIO.HIGH:
                    print("button5 released")
                    beep.standardSound()
                    dp.buttonpushsignal()
                    return 5
            if exitbutton_state != previous_exit_button_state:
                previous_exit_button_state = exitbutton_state
                if exitbutton_state == GPIO.HIGH:
                    print("exit released")
                    beep.standardSound()
                    dp.buttonpushsignal()
                    exit = not exit

    except KeyboardInterrupt:
        GPIO.cleanup()



