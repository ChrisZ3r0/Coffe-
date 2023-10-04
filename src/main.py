import features.read as read
import features.readcsv as data
import features.button as bt



def main():
    while True:
        bt.startbeep()
        print("Hello world!")
        if(read.rfidread()):
            bt.startbeep()
            print("Reading buttons to know wich coffe you get")
            bt.buttonpush()

        

        else:
            print("yeet again")


if __name__ == "__main__":
	main()