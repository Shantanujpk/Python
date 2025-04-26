# ----------------------------------------------
# Python Basics: Variables and Data Types
# ----------------------------------------------

# Variables:
# Variables are like containers that store data.
# Data can be of different types like string, integer, float, etc.
# Where is the container? -- It is stored in the system's RAM (memory).

# Example of different types of variables:

# Integer variable
a = 1  # Data type: int
print(a)

# String variable
b = "Ronaldo"  # Data type: str
print(b)

# Boolean variable
c = True  # Data type: bool
print(c)

# NoneType variable (represents the absence of a value)
d = None  # Data type: NoneType
print(d)

# Checking the type of each variable:
print("Type of a is", type(a))
print("Type of b is", type(b))
print("Type of c is", type(c))
print("Type of d is", type(d))

# ----------------------------------------------
# How Variables Work in Memory:
# When you write a = 1, Python stores the value 1 in memory (RAM)
# and assigns its address to variable 'a'.
# When you print 'a', Python goes to that address and retrieves the value 1.

# ----------------------------------------------
# Built-in Data Types in Python (with Examples)
# ----------------------------------------------

# 1. int (Integer): Whole numbers
num = 10
print(num, "=>", type(num))

# 2. float (Floating-point): Decimal numbers
pi = 3.14
print(pi, "=>", type(pi))

# 3. bool (Boolean): True or False
is_active = False
print(is_active, "=>", type(is_active))

# 4. str (String): Text
name = "Python"
print(name, "=>", type(name))

# 5. list (List): Collection of items (mutable)
fruits = ["apple", "banana", "cherry"]
print(fruits, "=>", type(fruits))

# 6. tuple (Tuple): Collection of items (immutable)
coordinates = (10, 20)
print(coordinates, "=>", type(coordinates))

# 7. dict (Dictionary): Key-Value pairs (Mapped Data)
student = {"name": "John", "age": 22}
print(student, "=>", type(student))

# ----------------------------------------------
# Important Note:
# - In Python, EVERYTHING is an Object.
# - Every data type you use (int, str, list, etc.) is actually a <class> which creates objects.
#
# Example:
# type(1) => <class 'int'>
# type("Hello") => <class 'str'>
#
# This means Python treats everything (even numbers and strings) as objects internally.
# ----------------------------------------------
