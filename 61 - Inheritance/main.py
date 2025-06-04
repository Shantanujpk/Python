# What is it? - OOPs concept which allows a child class to use properties of its parent class.
# When to use it? - When you want to reuse properties of a parent class and avoid creating a new class from scratch.
# How to use it? - child_class(parent_class)
# Types? - single, multiple, multilevel, hierarchical, hybrid.
# Single Inheritance: A child class inherits from a single parent class.
# Multiple Inheritance: A child class inherits from multiple parent classes.
# Multilevel Inheritance: A class inherits from a child class, creating a chain of inheritance.
# Hierarchical Inheritance: Multiple child classes inherit from the same parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance in a single program.


class parent_class1:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("I am in constructor of parent class")

    def parent_class_Details(self):
        print("I am in parent class function")
        print(f"Name is {self.name} and id is {self.id}")


class child_class(parent_class1):
    def __init__(self, name, id):
        # Call parent constructor
        super().__init__(name, id)
        print("I am in constructor of child class")

    def child_class_details(self):
        print("Child class method")
        print(f"id of {self.name} is {self.id}")

    def inherit_from_parent(self):
        print("I am in inheritance method, calling parent function:")
        self.parent_class_Details()


# Creating objects
e1 = parent_class1("Dan", 2)
e1.parent_class_Details()

print("\n")

e2 = child_class("Adam", 2)
e2.child_class_details()
e2.inherit_from_parent()  # Calls the method from parent class
