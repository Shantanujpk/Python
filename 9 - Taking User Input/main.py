# Taking Input from the User

# In Python, we use the input() function to take input from the user.
# NOTE: input() always returns the result as a string (even if you enter a number).

# Example:

a = input("Enter your favorite number: ")
print(a)
# 💡 Even though you entered a number, 'a' is still a string.

# Why is this important?
# → If you try to do math with it, it will not behave like a number.

# Another Example:

x = input("Enter First Number: ")
y = input("Enter Second Number: ")

print(x + y)
# ❗ Here, Python joins (concatenates) the two strings instead of adding them.

# How to fix it?
# → Use Type Casting to convert the input into integers.

# Correct Example:

print(int(x) + int(y))
# ✅ Now, x and y are converted to integers before adding.

# ---------------------------------------------------------------
# 🎯 Conclusion:
# Everything you get from input() is treated as a **string** by default.
# If you need to perform calculations, you must manually convert (type cast) it to int, float, etc.
