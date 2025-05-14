# How to raise error/ custome errors in python ?
# what are the custome erros: 

# custome error are the type of erros that is raised by user and which are not buit in errors to handle some userdefined or logical errors
# can be raised using  "raise" keyword 


# let take an input from user check the value is between 5 and 9 AND quit if it is then thow error 
# "Enter the correct value"
# 

a = input("Enter your value: ")

if a.lower() == 'quit':
    raise ValueError("You have entered 'quit', which is not allowed.")
elif a.isdigit():
    value = int(a)
    if 5 < value < 9:
        raise ValueError("Enter a value that is not between 6 and 8.")
else:
    raise ValueError("Invalid input. Please enter a number or 'quit'.")
