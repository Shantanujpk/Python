
#Operator Overloading is a feature in Python that allows you to define or change the behavior of standard operators (like +, -, *, etc.) for your own custom classes.
#It lets you use operators with objects of your own class just like with built-in types

"""
How it works ? 

What is Happening Internally?
When you write an expression like:
n1 + n2

Python does not understand what + means for custom objects like Number.
So behind the scenes, Python automatically calls a special method:
n1.__add__(n2)

That is what operator overloading means: defining how Python should behave when an operator is used on objects of your class
"""

class Number:
    def __init__(self, value):
        self.value = value

    # Operator overloading for '+' using __add__
    def __add__(self, other):
        # When n1 + n2 is used, this method is called
        return Number(self.value + other.value)

    # Operator overloading for '-' using __sub__
    def __sub__(self, other):
        # When n1 - n2 is used, this method is called
        return Number(self.value - other.value)

    #Operator overloading for '*' using __mul__
    def __mul__(self, other):
        # When n1 * n2 is used, this method is called
        return Number(self.value * other.value)

    # Operator overloading for '/' using __truediv__
    def __truediv__(self, other):
        # When n1 / n2 is used, this method is called
        return Number(self.value / other.value)

    # Operator overloading for '//' using __floordiv__
    def __floordiv__(self, other):
        # When n1 // n2 is used, this method is called
        return Number(self.value // other.value)

    # Operator overloading for '%' using __mod__
    def __mod__(self, other):
        # When n1 % n2 is used, this method is called
        return Number(self.value % other.value)

    # Operator overloading for '**' using __pow__
    def __pow__(self, other):
        # When n1 ** n2 is used, this method is called
        return Number(self.value ** other.value)

    # String representation for printing results
    def __str__(self):
        return str(self.value)


# Creating two Number objects
n1 = Number(10)
n2 = Number(3)

# Using overloaded operators (this calls the corresponding methods)
print("Addition:", n1 + n2)        # Calls __add__
print("Subtraction:", n1 - n2)     # Calls __sub__
print("Multiplication:", n1 * n2)  # Calls __mul__
print("Division:", n1 / n2)        # Calls __truediv__
print("Floor Division:", n1 // n2) # Calls __floordiv__
print("Modulus:", n1 % n2)         # Calls __mod__
print("Power:", n1 ** n2)          # Calls __pow__


