# ---------------------------------------------------
# 🕒 Python time module - Beginner Friendly Guide
# ---------------------------------------------------

# What is the time module?
# ➤ The time module in Python provides functions to work with time.
# ➤ It helps measure how long code takes to run, format date/time, pause execution, etc.

import time  # Import the built-in time module

# ---------------------------------------------------
# Measure time taken by a while loop
# ---------------------------------------------------
def whileloop():
    i = 0
    while i < 500:
        print(i)
        i = i + 1

# ---------------------------------------------------
# Measure time taken by a for loop
# ---------------------------------------------------
def forloop():
    for i in range(500):
        print(i)

# -----------------------------------------
# ⏱️ Time taken by the while loop
# -----------------------------------------
whilelooptime = time.time()  # Capture current time in seconds since epoch
print("Start time of while loop:", whilelooptime, "\n")

whileloop()  # Run the while loop

# Calculate and print the time taken to run the while loop
print("Time taken by while loop:", time.time() - whilelooptime)

# -----------------------------------------
# ⏱️ Time taken by the for loop
# -----------------------------------------
print("\nNow running the for loop...\n")

forlooptime = time.time()  # Capture time before for loop starts

forloop()  # Run the for loop

# Calculate and print the time taken to run the for loop
print("Time taken by for loop:", time.time() - forlooptime)

# ---------------------------------------------------
# 💤 time.sleep() - Pause execution
# ---------------------------------------------------
print("\nNow demonstrating time.sleep()...")
print("Waiting for 5 seconds...")

time.sleep(5)  # Pauses the program for 5 seconds

print("This line is printed after a 5-second delay.")

# ---------------------------------------------------
# 📅 time.strftime() - Format date/time
# ---------------------------------------------------
# time.localtime() gives the current local time as a structured object
t = time.localtime()
print("\nRaw local time structure:", t)

# strftime = string format time
# This formats the time in a readable string format like YYYY-MM-DD HH:MM:SS
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted current time is:", formatted_time)

# ---------------------------------------------------
# Summary:
# - time.time() → current timestamp (seconds since epoch)
# - time.sleep(x) → pause for x seconds
# - time.strftime() → format time to readable string
# - time.localtime() → get detailed current time info
# ---------------------------------------------------
