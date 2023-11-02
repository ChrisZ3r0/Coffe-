# Coffe+
 This is a school project. It will be calculating costs for a person, checking if you have the money through an RFID card reader.


# Requirements

1. Install `git` to clone the project

2. In raspi-config enable `I2C`:

```sudo raspi-config```

Here you have to navigate to interfacing options and then enable the I2C by selecting that.

3. You have to `install` the neccesery packages for the `RFID` reader

First, activate `SPI` interface

```sudo raspi-config```

Here you have to navigate to interfacing options and then enable the SPI by selecting that.

Now, you have to `restart` the raspberry pi

