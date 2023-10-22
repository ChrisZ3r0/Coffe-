from RPLCD.i2c import CharLCD
import time
from features import readcsv as text

def signals_initial():

    global startsignal
    startsignal = False
    global thankssignal
    thankssignal = False
    global coffesignal
    coffesignal = False


def lcdinitial():
    
    global lcd
    lcd = CharLCD('PCF8574', 0x27)

    lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
                  cols=16, rows=2, dotsize=8,
                  charmap='A02',
                  auto_linebreaks=True,
                  backlight_enabled=True)




# kave,available,price = text.load_coffe()
# for i in range(len(kave)):
#     lcd.write_string(str(kave[i])+ "\r\n \t\t\t\t\t\t")
#     lcd.write_string(str(price[i]) + " FT")
#     time.sleep(1)
#     lcd.clear()

def write_starting_message():
    lcdinitial()
    global startsignal
    
    lcd.write_string("Kartyat kerek")
    
    startsignal = False

def write_thanks_message():
    lcdinitial()
    global thankssignal
    lcd.clear()
    lcd.write_string("Koszonom")

    thankssignal=False

def write_coffee_and_price():
    lcdinitial()

    kave,available,price = text.load_coffe()

    print(coffesignal)
    for i, j in zip(kave,price):
        if not coffesignal:
            break
        
        lcd.clear()
        lcd.write_string("")
        lcd.write_string(str(i)+ "\r\n \t\t\t\t\t\t")
        lcd.write_string(str(j) + " FT")
        time.sleep(0.75)
        lcd.clear()
    

def display():
    signals_initial()
    while True:
        
        if startsignal:
            print("start")
            write_starting_message()
            time.sleep(0.5)

        elif thankssignal:
            print("thanks")
            write_thanks_message()
            time.sleep(1.5)

        elif coffesignal:
            print("coffee")
            write_coffee_and_price()
        


        time.sleep(0.1)

def Start_signal():
    global startsignal
    print("startsignal")
    startsignal = True

def Thanks_signal():
    global thankssignal
    print("thankssignal")
    thankssignal = True

def Coffe_signal():
    global coffesignal
    print("coffesignal")
    coffesignal = True

def buttonpushsignal():
    global coffesignal
    print("buttonpushsignal")
    coffesignal = False