import features.read as read
import features.readcsv as data
import features.button as bt
import features.beep as beep
import features.display as dp
import threading
import time 
#start_event = threading.Event()
#stop_event = threading.Event()

def main():

    
    display_thread = threading.Thread(target=dp.display)
    display_thread.start()


    beep.standardSound()
    while True:
        
        dp.Start_signal()
        print("Hello world!")
        if(read.rfidread()):
            dp.Thanks_signal()
            beep.goodSound()

            dp.Coffe_signal()


            print("Reading buttons to know wich coffe you get")
            bt.buttonpush()

        else:
            beep.errorSound()
            print("yeet again")


if __name__ == "__main__":
	main()