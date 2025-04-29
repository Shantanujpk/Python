# 📚 String Slicing in Python

# What is String Slicing?
# String slicing means selecting a part (substring) from a string.
# It helps you extract specific words or letters from a bigger string.

# 🛠 How to do String Slicing:
# Syntax:
# string_name[start_index:end_index]
# - start_index: Where slicing starts (included).
# - end_index: Where slicing stops (excluded).

# Remember:
# - Python indexing starts at 0.
# - len() function gives the total number of characters.

# 📦 Example:

length_of_string = "MasterPython"
print(len(length_of_string))  
# Output: 12

# 🎯 How to Slice:

print(length_of_string[0:11])  
# Output: MasterPytho
# (Includes characters from index 0 to 10, excludes 11.)

print(length_of_string[0:2])
# Output: Ma
# (Characters at index 0 and 1.)

# 💡 Shortcut Tip:
print(length_of_string[:11])
# Output: MasterPytho
# (If start is missing, Python assumes it as 0.)

# ➖ Using Negative Indexing:
print(length_of_string[:-6])
# Output: Master
# (Starts from 0 till index 6.)

# ❌ Wrong Slicing Example:
print(length_of_string[-2:-6])
# Output: (blank)
# (Slicing backwards without specifying step — gives empty output.)

# 🎯 Correct Negative Slicing Example:
print(length_of_string[-4:-1])
# Output: tho
# (From index 8 to 10.)

# 🧠 Quick Quiz:

nm = "Harry"
print(len(nm))
# Output: 5

print(nm[-4:-2])
# Output: ar
# (Indexes from -4 (1) to -2 (3), includes indexes 1 and 2.)

# ✅ Quick Summary Table (in words):
# string[0:4] => First 4 characters
# string[:4]  => Same as string[0:4]
# string[4:]  => From 5th character to end
# string[-4:-1] => 4th-last to 2nd-last character
# string[-2:-6] => Wrong slice, returns empty string
