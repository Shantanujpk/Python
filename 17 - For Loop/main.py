# 📘 For Loop in Python

# A 'for' loop is used to **iterate** over:
# - strings
# - numbers
# - lists
# - tuples
# - dictionaries
# - sets
# - anything that is iterable

# ------------------------------------------------------------------------------

# 🖥️ Example 1: Iterating over a STRING

name = "Honey"

# Instead of printing each character manually 5 times,
# we can simply use a for loop to automatically go through each character
for i in name:
    print(i)
# Output: H, o, n, e, y (each printed on a new line)

# ------------------------------------------------------------------------------

# 🖥️ Example 2: Iterating over a LIST

colours = ["Red", "Blue", "Yellow", "Purple"]

# Now let's print each color one by one
for colour in colours:
    print(colour)
    
    # Nested loop to print each character of the color
    for i in colour:
        print(i)
# Output:
# Red -> R, e, d
# Blue -> B, l, u, e
# and so on...

# ------------------------------------------------------------------------------

# 🖥️ Example 3: Printing NUMBERS from 0 to 19 using range()

# range(20) generates numbers starting from 0 up to 19
for i in range(20):
    print(i)
# Output: 0, 1, 2, ..., 19

# ------------------------------------------------------------------------------

# 🖥️ Example 4: Printing NUMBERS from 5 to 15 using range(start, end)

# range(5, 16) means start at 5 and go till 15 (16 is not included - it's n-1)
for i in range(5, 16):
    print("5 to 15 range is:", i)
# Output: 5, 6, 7, ..., 15

# ------------------------------------------------------------------------------

# 🖥️ Example 5: Printing NUMBERS up to 20,000

# If someone asks you "print numbers up to 20000" — easy!
for i in range(20001):
    print("range is:", i)
# ⚡ Note: This will print A LOT of numbers! (Be careful when running!)

# ------------------------------------------------------------------------------

# 🖥️ Example 6: Using STEP in range()

# Step controls **how big your jump** is in range().
# Syntax: range(start, stop, step)

# Example: Print even numbers from 2 to 98
for i in range(2, 100, 2):
    print(i)
# Output: 2, 4, 6, 8, ..., 98

# Explanation:
# - Start from 2
# - Go up to 100 (not included)
# - Jump 2 steps every time (so 2, 4, 6, 8, etc.)

# ------------------------------------------------------------------------------

# ✅ Quick Notes for Beginners:

# ➔ for VARIABLE in ITERABLE:
#      do something

# ➔ range(n)       --> numbers from 0 to n-1
# ➔ range(a, b)    --> numbers from a to b-1
# ➔ range(a, b, s) --> numbers from a to b-1, jumping s steps

# ➔ String is also an iterable (goes character by character)
# ➔ List is an iterable (goes element by element)
# ➔ Nested loops are allowed (loop inside loop)
# ➔ Step can be positive (forward ➡️) or negative (backward ⬅️)
