from RPLCD.i2c import CharLCD
import time
lcd = CharLCD('PCF8574', 0x27)

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)

lcd.write_string('Hello world')
time.sleep(2)
lcd.clear()
lcd.write_string('Hello\r\n  World!')
time.sleep(2)
lcd.clear()
lcd.write_string('Hello\n\r  World!')
time.sleep(2)
lcd.clear()
lcd.write_string('Helloworldhowa\n\rzoutodaaaz')
time.sleep(2)
lcd.clear()