"""
Difference between == and is

== it will compare the **values** of the variables 
is this will check the **exact location in the memory**

for mutable objects it can behave differently
"""

# example 1:
a = 5
b = "5"

print(a == b)  # false, because a is an integer and b is a string. The values are not equal.

print(a is b)  # false, because they are different types and stored in different memory locations.

# constant will be stored in only one location in python and other objects with the same value will be referred to it
# 5 in this case
x = 5
y = 5
print(x == y)  # True, because the values are both 5.
print(x is y)  # True, because small integers like 5 are stored in a shared memory location in Python.

# this is mutable so it will behave differently (to understand compare it to the first example)
c = [1, 2, 3]
d = [1, 2, 3]
print(c == d)  # true, because the **values** of the lists are the same.

print(c is d)  # false, because c and d are two different lists in different memory locations.

# Additional explanation for beginners:
# In Python:
# - "==" checks whether two things **look the same** (values).
# - "is" checks whether two things **are the same object** (memory location).

# For numbers and short strings (like '5' or 'hi'), Python may use the same memory for efficiency.
# But for bigger or more complex things (like lists, dictionaries), Python makes a new memory location even if they look the same.
