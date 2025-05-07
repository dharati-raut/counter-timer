

import time

# Ask the user to enter time in seconds
seconds = int(input("Enter the time in seconds: "))

# Countdown loop
while seconds > 0:
    print(f"Time left: {seconds} seconds")
    time.sleep(1)
    seconds -= 1

print("Time's up!")

#How it works (in simple words):

#1. Takes time input from the user

#2. Uses a while loop to count down

#3. Waits for 1 second each time using time.sleep(1)

#4. Ends with a “Time’s up!” message
