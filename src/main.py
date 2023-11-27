import features.read as read
import features.button as bt
import features.beep as beep
import features.display as dp
import threading
import time
import subprocess
import requests
import json

# Start the Flask app in a subprocess
flask_app_process = subprocess.Popen(["python", "flaskapp/app.py"])

def store_rfid_data(rfid_data):
    with open('/home/pi/Coffe-/data/shared_data.json', 'w') as file:
        json.dump({"rfid_data": rfid_data}, file)
        

def main():
    display_thread = threading.Thread(target=dp.display)
    display_thread.start()

    beep.standardSound()
    try:
        while True:
            dp.Start_signal()


            print("Hello world!")

            result,id=read.rfidread()
            store_rfid_data(id)
            
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
