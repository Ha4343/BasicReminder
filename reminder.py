import time
import random
import os

messages = [
    "Time for a quick break! 🚶‍♂️",
    "Stretch a little! 🧘‍♀️",
    "Drink some water! 💧",
    "Look away from the screen for 20 seconds! 👀",
    "Take a deep breath! 🌿",
]

def show_reminder():
    message = random.choice(messages)
    print(f"\n🔔 Reminder: {message}")  # Debug message
    if os.name == "nt":  # Windows
        os.system(f"msg * {message}")
    else:  # Mac & Linux
        cmd = f"osascript -e 'display notification \"{message}\" with title \"Break Time!\"'"
        print(f"Executing: {cmd}")  # Debug message
        os.system(cmd)

while True:
    wait_time = random.randint(10, 30)  # Reduced time for testing (10-30 sec)
    print(f"Waiting for {wait_time} seconds...")  # Debug message
    time.sleep(wait_time)
    show_reminder()
