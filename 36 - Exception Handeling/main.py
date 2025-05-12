# What is exception handling? 
# Exception handling is a process in which Python will allow user to handle errors/exception 
# and also make sure the code after that error runs

# It is used to avoid system crashing or stopping due to unexpected errors

# Exceptions in Python: 
# Python has multiple in-built exception handling features that help keep code running smoothly

# Syntax:

'''
try:
    # code here which might throw error
except:
    # if above code throws error it will catch that error/or lets say print the error
'''

# let's take an example to get table of user-given number

a = input("Enter a number: ")
print("Entered Number is:", a)

try:
    for i in range(0, 11):
        print(f"{int(a)} * {i} = {int(a) * i}")
    # what will happen if error occurs in above code?
    # the code below error will not execute without handling
    # how to deal with it? -> exception handling
except:
    print("Hmmm! Some error has occurred")

'''
Enter a number: as
Entered Number is : as
Hmmm! Some error has occurred

- what happened here is that I gave string instead of number so it errored out
- if there was no exception handling, the below code would not have executed
- but now it will!
'''

print("If there is exception handling or correct input, then only I will execute!!! Or else nopeeee")
