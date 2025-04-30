# 📘 What is If-Else in Python?

# If-Else is used to **make decisions** in Python programs.
# Based on whether a condition is True or False, Python decides which block of code to run.

# 🔹 'if' checks a condition.
# 🔹 'elif' checks another condition if the first 'if' is False.
# 🔹 'else' runs if none of the above conditions are True.

# 🔥 Important Comparison Operators:
# ==  → Equal to
# !=  → Not equal to
# <=  → Less than or equal to
# >=  → Greater than or equal to

# 🚨 Important:
# Indentation is **MANDATORY** in Python. (Usually 4 spaces are used)
# Without proper indentation, Python will give an error.

# 🎯 Nested If-Else:
# When an if-else block is **inside another if-else**, it is called Nested If-Else.

# ------------------------------------------------------------------------------

# 🖥️ Example: Taking age as input and deciding driving eligibility
a = int(input("Enter your age: "))  
# input() function always takes string input, so we convert it into integer using int() - type casting

print("Your age is:", a)

print(a == 18)  # Is 'a' equal to 18?
print(a <= 18)  # Is 'a' less than or equal to 18?
print(a >= 18)  # Is 'a' greater than or equal to 18?
print(a != 18)  # Is 'a' not equal to 18?

# Checking different conditions using if-elif-else
if (a <= 15):
    print("You cannot drive.")  # If age is 15 or less
elif (a <= 17):
    print("Take the driving test first.")  # If age is between 16 and 17
else:
    print("You can drive.")  # If age is 18 or more

# ------------------------------------------------------------------------------

# 🖥️ Quick Example: Nested If-Else
# One 'if' inside another 'if'

if (a > 10):
    if (a > 18):
        print("You are an adult.")  # If age is greater than 18
    else:
        print("You are a teenager.")  # If age is between 11 and 18
else:
    print("You are a child.")  # If age is 10 or less
