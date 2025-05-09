# Sets are unordered collection of data types,
# They store elements of multiple data types and return it in different order each time

# Items are separated with commas and enclosed in curly brackets
s = {"dan", 4, 85, 10.2, False}
print(s)  # Output order may change every time because sets are unordered


# How to check the type of a set using type() function?

s0 = {}
print(type(s0))  # <class 'dict'> 
# But why is it a dict and not a set?
# Yes, if you define an empty set using {}, it will be considered as a dictionary
# because {} by default represents an empty dictionary in Python

# So what to do?
# Use set() constructor to create an empty set

s1 = set()
print(type(s1))  # <class 'set'> — this is the correct way to create an empty set


# how to access elements from se? use for looop 

for i in s:
    print(i) # This will print element in set s and in any order