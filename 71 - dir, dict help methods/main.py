# Python built-in functions:
# dir()     -> Shows all the functions and attributes available for an object.
# __dict__  -> Returns a dictionary of all instance variables (data stored in the object).
# help()    -> Gives detailed documentation about an object (class, function, datatype etc.).

"""✅ dir() – "What can I do with this?"
Use When:

You want to see what operations or methods are available on a variable, object, or data type (like a list, string, class, etc.).

You're exploring a new library or class and want a quick glance at its capabilities.

Helpful For:

Debugging: Find if a method exists (e.g., does x have a sort() method?).

Learning: Understand what functions are tied to a class or datatype.

✅ __dict__ – "What does this object store?"
Use When:

You want to see the internal data (instance variables) of an object.

You're debugging and want to check what values are stored in a class instance.

Helpful For:

Inspecting the contents of custom objects (like classes you wrote).

Understanding what attributes an object has after it's been created.



khelp() – "I want full details/documentation"
Use When:

You're not sure what a function/class does, how to use it, or what parameters it takes.

You want to see the docstring, methods, and signature of a function or object.

Helpful For:

Understanding built-in functions (help(len)), or your own classes (help(Person)).

Getting a full explanation with descriptions and usage.

"""


# Let's start with a simple list:
x = [1, 2, 3, 4]  # A list with four elements

# Using dir() to print all the attributes and methods associated with a list
print("Using dir() on list:")
print(dir(x))  # Shows all methods (like append, pop, etc.) that can be used with lists

# Accessing a special method using its name
print("\nAccessing a special method:")
print(x.__class_getitem__)  # This shows the memory address or reference to the special method

# Now let's create a simple class
class Person:
    # Constructor: gets called when a new object of Person is created
    def __init__(self, name, id):
        self.name = name  # Store name in the object
        self.id = id      # Store id in the object

    # Method to display person's details
    def showdetails(self):
        print(f"name is {self.name} and id is {self.id}")

# Creating an object of the class Person
p = Person("Ram", 12)  # p is now a Person object with name "Ram" and id 12

print("\nUsing dir() on class object:")
print(dir(p))  # Lists all the attributes and methods available for this object

print("\nUsing __dict__ to see instance variables:")
print(p.__dict__)  # Shows the values stored in 'p', like {'name': 'Ram', 'id': 12}

print("\nUsing the help() function:")
print(help(p))  # Prints detailed help about the Person object, including class and methods
