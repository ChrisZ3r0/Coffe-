from RPLCD.i2c import CharLCD
import time
from features import readcsv as text

def initial():

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
    initial()

    lcd.write_string("Kartyat kerek")

def write_coffee_and_price():
    initial()

    kave,available,price = text.load_coffe()

    for i in range(len(kave)):
        lcd.clear()
        lcd.write_string("")
        lcd.write_string(str(kave[i])+ "\r\n \t\t\t\t\t\t")
        lcd.write_string(str(price[i]) + " FT")
        time.sleep(1)
        lcd.clear()