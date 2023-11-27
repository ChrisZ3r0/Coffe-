import features.read as read
import features.readcsv as data
import features.button as bt
import features.beep as beep
import features.display as dp
import threading
import time
import subprocess
import requests

# Start the Flask app in a subprocess
flask_app_process = subprocess.Popen(["python", "flaskapp/app.py"])


def send_rfid_to_flask(rfid_data):
    # Define the Flask app URL
    flask_app_url = "http://localhost:5000/read_rfid"

    # Send a POST request with RFID data
    response = requests.post(flask_app_url, data={"rfid_data": rfid_data})

    # Print the response (for debugging purposes)
    print("Flask app response:", response.text)


def main():
    display_thread = threading.Thread(target=dp.display)
    display_thread.start()

    beep.standardSound()
    
    try:
        while True:
            dp.Start_signal()


            print("Hello world!")

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
                send_rfid_to_flask(id)
            
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        dp.lcdclear()
        print("Stopping the Flask app...")
        flask_app_process.terminate()
        flask_app_process.wait()
        print("Flask app stopped.")

if __name__ == "__main__":
    main()
