# ------------------------------------------------------------
# Multiple Inheritance in Python
# ------------------------------------------------------------

# What is Multiple Inheritance?
# ➤ A child class can inherit features (properties and methods) from multiple parent classes.

# Why to Use It?
# ➤ When you want to combine functionalities from different, unrelated classes into one.

# When to Use It?
# ➤ When different classes provide unique features you need in a single child class.

# Advantages:
# ✅ Combines methods and properties from multiple classes
# ✅ Reduces code duplication
# ✅ Increases flexibility and reusability

# Disadvantages:
# ❌ Higher complexity
# ❌ Can lead to confusion if multiple parent classes have methods with the same name
# ❌ Dependency issues and method resolution conflicts

# ------------------------------------------------------------
# Parent Class 1: Employee
# ------------------------------------------------------------
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name of the employee is {self.name}")

# ------------------------------------------------------------
# Parent Class 2: Dance
# ------------------------------------------------------------
class Dance:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"Dance of the employee is {self.dance}")

# ------------------------------------------------------------
# Child Class: Inherits from both Employee and Dance
# ------------------------------------------------------------
class DanceEmployee(Employee, Dance):
    def __init__(self, name, dance):
        # Directly assigning attributes without calling super()
        # This can be dangerous if parent classes do more in __init__
        self.name = name
        self.dance = dance

    # No 'show' method here
    # So Python will follow MRO (Method Resolution Order)
    # and use 'show' from the first parent listed: Employee

# ------------------------------------------------------------
# Creating Object and Testing
# ------------------------------------------------------------
d = DanceEmployee("Dan", "HipHop")
d.show()  # Output: From Employee class → "Name of the employee is Dan"

# ------------------------------------------------------------
# Check Method Resolution Order (MRO)
# ------------------------------------------------------------
print(DanceEmployee.mro())
# Output: [<class '__main__.DanceEmployee'>, <class '__main__.Employee'>, <class '__main__.Dance'>, <class 'object'>]
# This shows Python will check methods in Employee before Dance

