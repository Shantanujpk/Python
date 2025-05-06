
# Let's learn about f-string 
# The primary use of f-string is to format the string in a coding-friendly way


#What is an f-string in Python?
#f-string (short for formatted string literal) is a way to insert variables and expressions directly inside a string, without using .format() or string concatenation. It was introduced in Python 3.6 and makes your code cleaner, shorter, and easier to read.

#✅ Why use f-strings?

#Easier to read and write
#No need to remember index positions like .format()
#You can insert variables directly inside curly braces {}
#Supports formatting numbers, dates, and even expressions inside the string

# Example without f-string 
# I want to pass name and country in a string 

string = "My name is {0} and I am from {1}"
name = "Dan"
country = "India"

# Let's use method format
print(string.format(name, country))  
# So here it will pass name at 0 and country at 1
# It will be very hard if I am passing more parameters,
# in that case, I will have to check the index of each parameter
# What to do?

# F-String:

string1 = f"My name is {name} and I am from {country}"  
# Here it will pass values of name and country automatically,
# so I don’t have to remember the index position.
print(string1)

# Can also use this in this way:
price = 1022.333
string2 = f"Value of the total price is {price:.2f}"  
# value of the total price is 1022.33 (rounded to 2 decimal places)
print(string2)

# What if I want to show as it is?
# Like what if I don’t want to pass the value but want to show how we use f-string
string3 = f"This is how I use f-string: My name is {{name}} and I am from {{country}}"
print(string3)  
# This is how I use f-string: My name is {name} and I am from {country}
