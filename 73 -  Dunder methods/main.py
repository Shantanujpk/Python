"""In Python, dunder methods (short for "double underscore" methods) are special methods with names that begin and end with double underscores, like __init__, __str__, and __add__. These methods allow you to define how your objects behave with built-in functions and operators, enabling customization of object behavior in a clean and intuitive way.
mathspp.com
datacamp.com
+1
mathspp.com
+1

🔹 What Are Dunder Methods?
Dunder methods, also known as magic methods, are predefined methods in Python that you can override to customize the behavior of your objects. They are invoked automatically by Python in response to certain operations. For example:
realpython.com

__init__: Called when an object is instantiated.

__str__: Called by the str() function and the print statement to compute the "informal" string representation of an object.

__add__: Called to implement the addition operation +.

By defining these methods in your classes, you can control how your objects interact with Python's syntax and built-in functions.
mathspp.com
+1
datacamp.com
+1

🔹 Common Dunder Methods and Their Uses
Here's a list of some commonly used dunder methods:
pythonmorsels.com

1. Object Initialization and Construction
__new__(cls, [...]): Called to create a new instance of a class.

__init__(self, [...]): Called to initialize a new instance.

__del__(self): Called when an object is about to be destroyed.
youtube.com
+3
scaler.com
+3
geeksforgeeks.org
+3
geeksforgeeks.org

2. String Representation
__str__(self): Called by str() and print to compute the "informal" string representation.

__repr__(self): Called by repr() to compute the "official" string representation.
realpython.com
+2
mathspp.com
+2
scaler.com
+2

3. Arithmetic Operations
__add__(self, other): Defines behavior for the addition operator +.

__sub__(self, other): Defines behavior for the subtraction operator -.

__mul__(self, other): Defines behavior for the multiplication operator *.

__truediv__(self, other): Defines behavior for the division operator /.
realpython.com
+3
mathspp.com
+3
geeksforgeeks.org
+3

4. Comparison Operations
__eq__(self, other): Defines behavior for the equality operator ==.

__ne__(self, other): Defines behavior for the inequality operator !=.

__lt__(self, other): Defines behavior for the less-than operator <.

__le__(self, other): Defines behavior for the less-than-or-equal-to operator <=.

__gt__(self, other): Defines behavior for the greater-than operator >.

__ge__(self, other): Defines behavior for the greater-than-or-equal-to operator >=.
youtube.com
+2
geeksforgeeks.org
+2
mathspp.com
+2

5. Container Methods
__len__(self): Called by len() to determine the length of the object.

__getitem__(self, key): Called to retrieve an item using the obj[key] syntax.

__setitem__(self, key, value): Called to set an item using the obj[key] = value syntax.

__delitem__(self, key): Called to delete an item using the del obj[key] syntax.

__contains__(self, item): Called by the in operator to check for membership.

6. Callable Objects
__call__(self, [...]): Allows an instance of a class to be called as a function.

7. Context Management
__enter__(self): Called when entering a with statement context.

"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v3)             # Output: Vector(6, 8)
print(v1 == v2)       # Output: False


"""Dunder methods allow your custom classes to integrate seamlessly with Python's built-in operations and functions. By implementing these methods, you can:
datacamp.com

Make your objects behave like built-in types.

Enable operator overloading to define custom behavior for operators.

Control object creation, representation, and destruction.

Implement custom container types that support iteration, indexing, and membership tests.

Create callable objects and context managers for resource management.
datacamp.com
pythonmorsels.com

Understanding and utilizing dunder methods can lead to more intuitive and Pythonic code, especially when designing classes that model complex behaviors or data structures."""