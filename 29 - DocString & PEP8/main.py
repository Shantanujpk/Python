# What is DOCString:
# It is a string that will be just below the function definition or just above the function body
# It is a string that gives a description of the function, useful for understanding what the function does
# Difference between docstring and comment: DocString cannot be ignored while comments can
# Also, changes in comments do not affect the code, but changes in the docstring can affect documentation tools

# Example:

def docString(n):
    '''takes number as input and gives square'''
    print(n * n)

docString(5)  # 25

# But if I do this, it will print the docstring also:
print(docString.__doc__)  # takes number as input and gives square


# What if I add something just below function definition and above docstring?
# In this case, the docstring will not be recognized and its value will be None

def docString0(n):
    print("Just above the docstring")
    '''takes number as input and gives square'''
    print(n * n)

docString0(5)  # 25

# But if I do this, it will print the docstring also:
print(docString0.__doc__)  # None, that is why the location of the docstring is important


# Now what is PEP8:
# PEP 8 is called Python Enhancement Proposal
# Basically used to make your code more readable and easy to understand

# How to use: 
# Run `import this` in your Python shell
# It will give you a poem by Tim Peters — once you're done with your project, you'll realize what it means

import this  # 🐍

'''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''