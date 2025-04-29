# Let's Talk About Strings

# What is a string?
# → A string is a group of characters put together.

# Example:

print("This is a string")

# Taking a string input from user
name = input("Enter your name: ")
print(name)

# You can also use single quotes ' '
last_name = 'Jpk'
print(last_name)

# You can also use triple quotes ''' ''' for multi-line strings

multiline_string = '''Hi, My name is Shan
I am a master's student
Mastering Python
and helping others to do the same!!!'''

print(multiline_string)

# ---------------------------------------------------------------

# Let's Talk About Indexing

# In Python, indexing starts from 0.
# It means the first character is at position 0, the second at 1, and so on.

# Example:

print(name[0])  # First character
print(name[1])  # Second character
print(name[2])  # Third character
print(name[3])  # Fourth character

# ❗ Problem:
# If the string is very large (like a multiline string), checking each index manually takes too much time.

# Solution:
# Use a loop to go through each character automatically.

# Example:

for i in multiline_string:
    print("Every character in the Multiline String:", i)

# 🎯 Note:
# → The loop will also include spaces and newline characters (\n) as part of the string.
