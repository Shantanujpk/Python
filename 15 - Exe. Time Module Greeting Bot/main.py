# 📘 What is the time module in Python?
# - time module allows you to work with dates, times, and delays in Python.
# - You can get the current system time, pause your program, measure time, etc.

import time  # Import the time module (built-in Python library)

# ------------------------------------------------------------------------------

# 🖥️ Getting the current system time
current_time = time.localtime()  # This gets the current local time in struct_time format
print(current_time)  # Print full time info (like year, month, day, hour, minute, second)

# ------------------------------------------------------------------------------

# 🖥️ Formatting the current time into a readable string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# %Y → Year
# %m → Month
# %d → Day
# %H → Hour (24-hour clock)
# %M → Minute
# %S → Second

print(formatted_time)  # Example: '2025-04-29 14:30:45'

# ------------------------------------------------------------------------------

# 🖥️ Extracting hour, minute, and second separately

# Get current hour as integer
hr = int(time.strftime("%H", time.localtime()))  

# Get current minute as integer
min = int(time.strftime("%M", time.localtime()))  

# Get current second as integer
sec = int(time.strftime("%S", time.localtime()))  

print(hr, min, sec)  # Print the current hour, minute, and second separately

# ------------------------------------------------------------------------------

# 🖥️ Deciding whether it's morning, afternoon, or evening based on the time

# If hour is less than 12 (morning) and minutes and seconds are 0 or less
if (hr < 12 ):
    print("Good Morning")

# If hour is 12 or more (afternoon) and minutes and seconds are positive
elif (hr >= 12 and min >= 0 and sec >= 0):
    print("Good Afternoon")

# If hour is 18 or more (evening time) and minutes and seconds are positive
elif (hr >= 18 and min >= 0 and sec >= 0):
    print("Good Evening")

# If none of the above conditions match
else:
    print("Clock is not working")

# ------------------------------------------------------------------------------

# 🔥 Important Note:
# - localtime() returns time based on your computer’s local timezone.
# - struct_time contains: year, month, day, hour, minute, second, etc.
# - strftime() is used to convert struct_time into human-readable format.
# - You can extract specific parts like hour, minute, and second easily using strftime codes.

# 📌 strftime format codes quick reference:
# %Y → Year  (2025)
# %m → Month (01-12)
# %d → Day   (01-31)
# %H → Hour  (00-23) [24-hour format]
# %I → Hour  (01-12) [12-hour format]
# %M → Minute (00-59)
# %S → Second (00-59)
# %p → AM/PM (for 12-hour clock)

