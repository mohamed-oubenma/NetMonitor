import os
import time
from datetime import datetime
from plyer import notification
import winsound
import threading


def send_alert():
    notification.notify(
        title="Look away!",
        message="Look away from the screen for 20 seconds!",
        app_name="Look Away",
        timeout=60,  # seconds
        app_icon="icon.ico"  # Path to your icon file
    )

# Define a function that will run in the thread
def worker():
    while True:
        time.sleep(7200)  # Wait for 2 hours
        send_alert()

# Create a thread
thread = threading.Thread(target=worker)

# Start the thread
thread.start()

# Settings
CHECK_INTERVAL = 300  # seconds between checks
RELIABLE_HOST = "8.8.8.8"  # Google's public DNS server

def is_internet_up():
    return os.system(f"ping -n 1 {RELIABLE_HOST} > nul") == 0  # For Windows, use '-n'



def paly_sound():
    # Path to your sound file
    sound_file = "alarm.wav"

    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

    # Wait for user input to stop
    input("Press Enter to stop the alarm...")
    winsound.PlaySound(None, winsound.SND_ASYNC)  # Stop the sound

while True:
    time.sleep(CHECK_INTERVAL)
    if not is_internet_up():
        time.sleep(30)
        if not is_internet_up():
            print("internet is down" )
            # send_alert()
            paly_sound()
    else:
        print("internet is up: " + str(datetime.now()))
