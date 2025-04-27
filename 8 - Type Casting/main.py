# Let's dive into Type Casting
# What is Type Casting?
# → Type casting means converting one data type into another data type.

# How do we do it?
# → Using functions like int(), str(), ord(), dict(), hex(), oct(), tuple(), set(), list(), etc.

# Why is Type Casting useful?
# → It helps change the data type of a variable so that it behaves correctly in operations.
# → Example: If a number is stored inside quotes (" "), it is considered a STRING.
# → If we try to add two strings, Python joins them instead of adding the numbers.

# Let's see an example:

a = "2"
b = "5"

print(a + b)  # Output: "25"
# ⚡ Here Python treated a and b as strings and simply joined them, NOT added!

# How to fix this?

a = "2"
b = "5"

print(int(a) + int(b))  # Output: 7
# 💡 By using int(), we changed "2" and "5" from strings to integers before adding.

# ---------------------------------------------------------------
# Two Types of Type Casting:

# 1. Explicit Type Casting
# → We manually tell Python to convert the data type.
# Example:
a = "2"
b = "5"
print(int(a) + int(b))  # Here we explicitly converted from string to int.

# 2. Implicit Type Casting
# → Python automatically converts the data type based on the situation.
# → Python follows a "data type order" to avoid data loss (like int → float if needed).

# Example:
d = 9.9  # Float data type
e = 1    # Integer data type
print(d + e)  # Output: 10.9
# 🧠 Here, Python automatically converted 'e' from int to float.
# Final result is float because float has a higher order than int in Python.

