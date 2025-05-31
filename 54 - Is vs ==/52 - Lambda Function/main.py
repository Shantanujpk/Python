# Lambda Function

# A variable that can be use as fucntion 
# It is used to pass function as argument 

"""📌 What is a Lambda Function?
A lambda function is a small, anonymous function in Python, defined using the lambda keyword.

Unlike regular functions created with def, a lambda function doesn’t have a name (though it can be assigned to a variable).

📌 Why do we use it?
To create short, quick functions without the need for a full def block.

Great for one-liners or when a function is used only once (like in sorting or filtering data).

Commonly used with functions like map(), filter(), and reduce().

📌 How helpful is it?
✅ Makes code shorter and more concise for simple operations.
✅ Improves readability when working with inline transformations.
✅ Reduces clutter—no need to define a full function if it’s only needed in one spot!

"""

# Syntax:  lambda arguments: expression


# I want to define a function for addition 

# Define a function to add two numbers
def sum(a, b):
    return a + b

# Call the sum function with arguments 1 and 1
print(sum(1, 1))

# Create a lambda function that adds two numbers
sum_lambda = lambda x, y: (x + y)

# Call the lambda function with arguments 2 and 2
print(sum_lambda(2, 2))

# Define a function to calculate the average of three numbers
def avg(j, k, l):
    return ((j + k + l) / 3)

# Call the avg function with arguments 8, 8, and 8
print(avg(8, 8, 8))

# Create a lambda function to calculate the average of three numbers
avg_lambda = lambda t, r, e: (t + r + e) / 3

# Call the lambda function with arguments 9, 9, and 9
print(avg_lambda(9, 9, 9))

# Define a function that takes a number (cube) and another number (g), adds them together
def cube(cube, g):
    return cube + g

# Create a lambda function to calculate the cube of a number
cube_lambda = lambda d: d * d * d

# Call the cube function, passing the cube of 5 and adding 10
print(cube(cube_lambda(5), 10))
