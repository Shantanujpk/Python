# Function is a block of code that executes whenever called 

# Why do we need functions?
# Suppose you are working on a code where you need to add two numbers 100 times.
# Will you write the same addition code 100 times? No!
# You’ll write it once as a function and just call it wherever needed.

# ✅ Benefits of using functions:
# - Easy to reuse code
# - Reduces repetition
# - Improves code readability
# - Essential for large programs
# - Helps in writing cleaner and more organized code

# Example of built-in functions: print(), max(), len(), etc.

# Now let’s say we want to calculate the Gmean (Geometric Mean) of two numbers.
# First, let’s do it without a function:

a = 10
b = 10
gmean = (a * b) / (a + b)
print(gmean)

# OK. Now if we want to calculate it again for different numbers,
# should we write the same code again? No!
# We’ll define a function for it.

# ✅ Syntax to define a function:
# def function_name(parameters):
#     # code block

# Defining a function to calculate Gmean
def calculateGmean(a, b):
    gmean = (a * b) / (a + b)
    print(gmean)

# Now let’s call the function with different sets of numbers
calculateGmean(12, 12)
calculateGmean(12, 112)
calculateGmean(14322, 112)

# ✅ So above, we calculated Gmean for multiple number pairs in just 3 lines of code
# That’s the power of using functions in programming!


# 🔸 Now, what if we want to check which number is greater?
# One way is to use simple if-else (without function):

if a > b:
    print("A is greater")
else:
    print("B is greater")

# But what if we want to check it again for different numbers like c and d?
# Should we write the same if-else again? No!
# Let’s define a function for it.

# Function to check which number is greater
def greaterNumber(a, b):
    if a > b:
        print("A is greater")
    else:
        print("B is greater")

# ✅ Important: You must define the function *before* calling it
# Otherwise, you’ll get a "function not defined" error

# ✅ What if I want to define a function now, but write the body later?

# If you define a function but forget to write the body,
# Python will throw an error (IndentationError or SyntaxError)

# ❌ This will cause an error:
# def someFunction(a, b):
#     # no code here

# ✅ Solution: Use the `pass` statement
# The `pass` keyword is a placeholder — it tells Python: "do nothing for now"

def passFunction(a, b):
    pass  # This tells Python to skip the body for now without error

# Later, you can come back and write the actual logic here


# Now let’s call both functions for different values
calculateGmean(12, 13)
greaterNumber(12, 13)

calculateGmean(12, 112)
greaterNumber(12, 112)

calculateGmean(14322, 112)
greaterNumber(14322, 112)


# ✅ Types of Functions in Python:

# 1️⃣ Built-in Functions:
# These functions are already provided by Python.
# You do NOT need to define them. You can directly use them.

# Examples of built-in functions:
print("This is a built-in function")       # Prints output
max_value = max(5, 10, 3, 9)               # Returns the maximum value
print("Max value:", max_value)

min_value = min(5, 10, 3, 9)               # Returns the minimum value
print("Min value:", min_value)

length = len("Hello")                      # Returns length of string
print("Length of word:", length)

numbers = list(range(5))                   # Creates a list [0, 1, 2, 3, 4]
print("List:", numbers)

my_dict = dict(name="Kartik", age=25)      # Creates a dictionary
print("Dictionary:", my_dict)


# 2️⃣ User-defined Functions:
# These are functions created by the user to perform custom tasks.

# Example 1: A function to calculate Gmean
def calculateGmean(a, b):
    gmean = (a * b) / (a + b)
    print("Gmean is:", gmean)

# Example 2: A function to find the greater number
def greaterNumber(a, b):
    if a > b:
        print("A is greater")
    else:
        print("B is greater")

# Calling user-defined functions
calculateGmean(10, 20)
greaterNumber(45, 30)

# ✅ So, Python has both built-in functions and user-defined functions.
