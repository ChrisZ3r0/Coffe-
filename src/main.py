import features.read as read
import features.readcsv as data
import features.button as bt
import features.beep as beep


def main():
    beep.standardSound()
    while True:
        print("Hello world!")
        if(read.rfidread()):
            beep.goodSound()
            print("Reading buttons to know wich coffe you get")
            bt.buttonpush()

        

        else:
            beep.errorSound()
            print("yeet again")


if __name__ == "__main__":
	main()