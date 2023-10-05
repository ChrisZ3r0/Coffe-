import features.read as read
import features.readcsv as data
import features.button as bt
import features.beep as beep
import features.display as dp

def main():
    beep.standardSound()
    while True:
        dp.write_starting_message()
        print("Hello world!")
        if(read.rfidread()):
            dp.write_thanks_message()
            beep.goodSound()
            dp.write_coffee_and_price()
            print("Reading buttons to know wich coffe you get")
            bt.buttonpush()

        

        else:
            beep.errorSound()
            print("yeet again")


if __name__ == "__main__":
	main()