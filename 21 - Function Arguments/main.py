# ✅ What are Function Arguments?

# Arguments are values you pass into a function when calling it.
# There are 4 types of function arguments in Python:
# 1. Default Arguments
# 2. Required (Positional) Arguments
# 3. Keyword Arguments
# 4. Variable-length Arguments (*args, **kwargs)

# 🔹 1. Default Arguments:
# These are values that are automatically used if no value is provided by the user.
# Useful when you want a function to work with some default values.

def addition(a=10, b=19):  # a and b have default values
    result = a + b
    print("Addition is:", result)

# ✅ Now let's call this function in different ways

addition()           # No values passed → a = 10, b = 19 (default)
addition(1, 1)       # a = 1, b = 1 → overrides default values
addition(12)         # Only a is passed → a = 12, b = 19 (b remains default)
addition(b=11)       # Only b is passed using keyword → a = 10 (default), b = 11


# 🔹 2. Keyword Arguments

# In keyword arguments, you mention the name of the parameter while passing the value.
# ✅ The order of arguments does NOT matter in this case.
# You can pass them in any order, and Python will match them by name.

def addition(a=10, b=19):
    result = a + b
    print("Addition is:", result)

# ✅ Calling function using keyword arguments
addition(b=12, a=100)  # Even though b comes before a, Python matches the names → a=100, b=12

# 🔹 3. Required (Positional) Arguments

# These are the arguments that you MUST pass when calling the function.
# If you don't provide them, Python will throw an error.

# Also, when you're not using keyword arguments, the order of arguments matters!

def addition(a, b=19):  
    # 'a' is a required argument → MUST be passed
    # 'b' has a default value → optional
    result = a + b
    print("Addition is:", result)

# ✅ Calling the function
addition(2)         # a = 2 (required), b = 19 (default)
addition(5, 15)     # a = 5, b = 15 → both values passed
# addition()       ❌ This would throw an error because 'a' is required

# 🔹 4. Variable-length Arguments

# Sometimes you don’t know how many arguments will be passed to the function.
# In that case, you can use *args (or any name with a * in front) to accept multiple values.

# These values are stored as a tuple inside the function.

def addition(*numbers):  
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Addition is:", sum)

# ✅ Calling the function with multiple arguments
addition(5, 15, 12, 12, 234, 345, 12)  # All values go into the 'numbers' tuple


# 🔹 What is a return statement?

# So far, our functions were only printing the result.
# But what if we want to STORE the result and use it later?
# For that, we use the `return` keyword.

# ✅ A function with return gives back a value to the caller.
# We can then store this value in a variable and use/print it anytime.

def addition(*numbers):  
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum  # Return the final sum instead of printing it

# ✅ Calling the function and storing the result
result = addition(5, 15, 12, 12, 234, 345, 12)  # The sum is returned and stored in 'result'

# ✅ Now we can print or use it later
print("Returned result is:", result)
