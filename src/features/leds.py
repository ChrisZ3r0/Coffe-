import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

GPIO.setup(31,GPIO.HIGH)
GPIO.setup(32,GPIO.HIGH)
GPIO.setup(29,GPIO.HIGH)
GPIO.setup(26,GPIO.HIGH)
GPIO.setup(7,GPIO.HIGH)


print("LED on")

GPIO.setup(31,GPIO.HIGH)
print("led1")
time.sleep(5)
GPIO.setup(31,GPIO.LOW)

GPIO.setup(32,GPIO.HIGH)
print("led2")
time.sleep(5)
GPIO.setup(32,GPIO.LOW)

GPIO.setup(29,GPIO.HIGH)
print("led3")
time.sleep(5)
GPIO.setup(29,GPIO.LOW)

GPIO.setup(26,GPIO.HIGH)
print("led4")
time.sleep(5)
GPIO.setup(26,GPIO.LOW)

GPIO.setup(7,GPIO.HIGH)
print("led5")
time.sleep(5)
GPIO.setup(7,GPIO.LOW)

print("LED off")
