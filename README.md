# Coffe+
 This is a school project. It will be calculating costs for a person, checking if you have the money through an RFID card reader.


# Requirements

1. Install `git` to clone the project

2. In raspi-config enable `I2C`:

```
sudo raspi-config
```

Here you have to navigate to interfacing options and then enable the I2C by selecting that.

3. You have to `install` the neccesery packages for the `RFID` reader

First, activate `SPI` interface

```
sudo raspi-config
```

Here you have to navigate to interfacing options and then enable the SPI by selecting that.

Now, you have to `restart` the raspberry pi

You can check if it activated correctly with this: 

```
lsmod | grep spi
```

If you see `spi_bcm2835` then everything should be good

If not, then just do:

```
sudo nano /boot/config.txt
```

and then search for `dtparam=spi=on`. If it has a `#` before it, just remove it.

If you cannot find this text, then just add it at the end of the `config.txt`

For you to use this RFID, you have to run some commands in the terminal.

Firstly:

```
sudo apt update 
sudo apt upgrade
```

After that zou have to install these packages:

```
sudo apt install python3-dev python3-pip
```

And lastly, you have to use these 2 commands:

```
sudo pip3 install spidev
```
```
sudo pip3 install mfrc522
```

Now everything should be installed, and you can test your RFID card reader.

4. 