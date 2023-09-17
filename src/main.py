import features.read as read
import features.readcsv as data
import features.button as bt



def main():
    print("Hello world!")
    if(read.rfidread()):
        print("Reading buttons to know wich coffe you get")
        bt.buttonpush()

        

    else:
        print("yeet again")


if __name__ == "__main__":
	main()