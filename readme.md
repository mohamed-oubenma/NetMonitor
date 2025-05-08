# Internet Checker Script

This script periodically checks the status of your internet connection and alerts you if the connection is down. Additionally, it reminds you to take breaks from your screen every 2 hours.

**Note:** This script is designed to work on **Windows** only.

## Features

1. **Internet Connection Check**:
    - The script pings a reliable host (Google's public DNS server) every 5 minutes to check if the internet is up.
    - If the internet is down, it waits for 30 seconds and checks again.
    - If the internet is still down, it prints a message and plays an alarm sound until the user stops it by pressing Enter.

2. **Screen Break Reminder**:
    - Every 2 hours, the script sends a desktop notification reminding you to look away from the screen for 20 seconds.
    - The reminder runs in a separate background thread.

## Dependencies

- `plyer`: Used for sending desktop notifications.
- `winsound`: Used for playing sound alerts (Windows only).
- `threading`: Used to run the screen break reminder in a separate thread.

## How to Use

1. Ensure you have the required dependencies installed:
    ```sh
    pip install plyer
    ```

2. Run the script:
    ```sh
    python checker.py
    ```