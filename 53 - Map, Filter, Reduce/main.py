"""📌 What is map()?
map() is a built-in Python function that applies a given function to each item in an iterable (like a list, tuple, etc.).

It’s part of Python’s functional programming toolkit.

📌 Why do we use it?
To apply the same operation to all items in a collection efficiently and cleanly.

It’s a more concise and readable alternative to writing a for loop."""

# map functiuon applies a function to each element in the sequence and returns new sequence 
# example squre of each element in a list 
from functools import reduce

def squre (x):
    return x*x

l = [1,2,3,4,5,6]
newl =[]

for item in l:
    newl.append(item*item)
print (newl)

# i can do the same thing in one line 
# use map 

newl1= list(map(squre,l))
print("Used map here!!")
print(newl1)

newl2 = list(map(lambda x : x*x , l)) # no nned to pass a funciton here !!! 
print (newl2)

"""📌 What is filter()?
filter() is a built-in Python function that lets you filter out elements from an iterable based on a condition (a function that returns True or False).

📌 Why do we use it?
To create a new iterable with only the items that meet certain criteria.

It’s an efficient way to remove unwanted elements from a list or other collection.
"""

def filter_function(a):
    return a>5
    
newl3 = list(filter(filter_function,l))
print(newl3)

newl4 = list(filter(lambda y : y>5 , l))
print (newl4)


"""📌 What is reduce()?
reduce() is a function from Python’s functools module that applies a rolling computation to a sequence of elements, combining them into a single result.

📌 Why do we use it?
To accumulate or reduce a sequence of values into a single result (like sum, product, or custom aggregations).

It’s especially useful when you want to combine elements with an operation (e.g., adding or multiplying) sequentially.
"""
# reduce
# takes two argument ad returns a single value 

listr = [1,2,3,4,5,6,7,8]

reduced_list = reduce(lambda x , y : x + y,listr )
print(reduced_list)