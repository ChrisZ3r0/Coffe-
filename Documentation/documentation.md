# Ez itt a Coffee+ projekt dokumnetációja

## Bekötési rajz

![A pinek bekötése](../../Pictures/Coffe+schematik.png)

### A pinek bekötési rendje
RFID

    SDA → 24    
    SCK → 23
    MOSI → 19
    MISO →  21
    GND → táp
    RST → 22
    3.3v → táp

Buzzer

    pin 16

Buttons

    pin 40,
    pin 38,
    pin 36,
    pin 37,
    pin 35,
    pin 33,
    
Minden eszköz GND lábát a GND line-ra kötjük a tápegységen

Egy Led be van kötve, ellenállással csak az áramkörbe, hogy tudjuk hogy az eszköz áram alatt van.

I2C Display

    GND → táp
    VCC → táp
    SDA → pin 3
    SCL → pin 5
