import features.read as read
import features.readcsv as data
import features.button as bt
import features.beep as beep
import features.display as dp
import threading
import time
import subprocess

# Start the Flask app in a subprocess
flask_app_process = subprocess.Popen(["python", "flaskapp/app.py"])

def main():
    display_thread = threading.Thread(target=dp.display)
    display_thread.start()

    beep.standardSound()
    
    try:
        while True:
            dp.Start_signal()
            #print("Hello world!")
            result,id=read.rfidread()
            if result:
                #print(id)
                dp.Thanks_signal()
                beep.goodSound()
                dp.Coffe_signal()

                print("Reading buttons to know which coffee you get")
                bt.buttonpush(id)

            else:
                beep.errorSound()
                dp.carderror()
                print("Try again")
            
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        dp.lcdclear()
        print("Stopping the Flask app...")
        flask_app_process.terminate()
        flask_app_process.wait()
        print("Flask app stopped.")

if __name__ == "__main__":
    main()
