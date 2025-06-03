# -----------------------------------------------------------------------------
# 🎨 Decorators in Python
# -----------------------------------------------------------------------------
# What is it?
# A decorator is a function that takes another function as an argument, 
# adds some extra functionality to it, and returns a new function.
#
# Why we use it?
# - To add behavior to existing functions without modifying their code.
# - Great for cross-cutting concerns like logging, authentication, etc.
#
# How to use it?
# - Define a decorator function (which takes a function as a parameter).
# - Inside, define a nested function that adds extra behavior.
# - Use the @decorator_name syntax above your target function.
#
# When to use it?
# - When you want to apply the same functionality to multiple functions 
#   (e.g., timing, logging, error handling).
# - When you want to keep your main function code clean.

# -----------------------------------------------------------------------------
# 🐍 Example Decorator
def deco(dec): # dec is the function taken as argument
    # Inner wrapper function that adds extra functionality
    def mdec(*args, **kwargs):
        print(f"Hi! You are in {dec.__name__} function!")
        dec(*args, **kwargs)  # Call the original function
        print("Thank you for using the function!")
    return mdec  # Return the new function

# -----------------------------------------------------------------------------
# 🧩 Example 1: Decorating a function without arguments
@deco
def hello():
    print("Function without arguments")

# -----------------------------------------------------------------------------
# 🧩 Example 2: Decorating a function with arguments
@deco
def addition(a, b):
    print("Function with arguments")
    print(f"Addition of {a} and {b} is", a + b)

# -----------------------------------------------------------------------------
# 🧪 Let’s see them in action!

print("\nCalling hello():")
print(hello())  # Will show the decorator behavior

print("\nCalling addition(10, 10):")
addition(10, 10)  # Will show the decorator behavior + addition result

# -----------------------------------------------------------------------------
# 🚀 Explanation of *args and **kwargs
# -----------------------------------------------------------------------------
# - *args: Allows you to pass a variable number of positional arguments to a function.
# - **kwargs: Allows you to pass a variable number of keyword arguments (key=value pairs).
#
# Why we use them?
# - To make functions more flexible and accept any number of inputs.
#
# How to use them?
# - In function definitions: def func(*args, **kwargs)
# - In function calls: func(*args, **kwargs) will unpack the values.
#
# When to use them?
# - When writing decorators (like in our example) to make sure they work with
#   any function signature (no matter how many parameters).
# - When you’re not sure how many arguments will be passed to a function.

# -----------------------------------------------------------------------------
# 🌟 My Favorite Part
# Decorators are like magical wrappers — they make your functions fancier 
# without changing the original code. They’re great for adding reusable 
# features to many functions! ✨

