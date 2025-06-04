"""🟩 What is it?
Getters and setters are special methods in classes:

Getter: a method to get or read the value of a private attribute.

Setter: a method to set or update the value of a private attribute.

🟦 Why to use it?
🛡️ To protect your data (encapsulation).

🧪 To add extra logic when getting or setting a value (like validation or logging).

⚙️ To control how a variable is accessed or modified.

🟨 When to use it?
If you want to hide the actual variable from outside the class (like _name instead of name).

If you need to validate data before updating (like checking if salary is not negative).

If you want to add logic every time someone reads or updates a variable (like logging, calculations, or transformations)."""


# 🟢 Example 1: Basic getter and setter methods

class Person:
    def __init__(self, name):
        # Using an underscore to show it's meant to be "private"
        self._name = name

    # Getter method
    def get_name(self):
        print("Getting name...")
        return self._name

    # Setter method
    def set_name(self, new_name):
        print("Setting name...")
        self._name = new_name

# Using the getter and setter
print("=== Example 1: Basic Getter and Setter Methods ===")
person1 = Person("Alice")

# Get name
print(person1.get_name())  # Output: Alice

# Set name
person1.set_name("Bob")
print(person1.get_name())  # Output: Bob

print("\n")


# 🟠 Example 2: Using @property decorator (Pythonic way)

class Car:
    def __init__(self, brand):
        self._brand = brand

    # Getter method
    @property
    def brand(self):
        print("Getting brand...")
        return self._brand

    # Setter method
    @brand.setter
    def brand(self, new_brand):
        print("Setting brand...")
        self._brand = new_brand

print("=== Example 2: Using @property Decorator ===")
car1 = Car("Toyota")

# Get brand (like an attribute)
print(car1.brand)  # Output: Toyota

# Set brand (like an attribute)
car1.brand = "Honda"
print(car1.brand)  # Output: Honda

print("\n")


# 🔵 Example 3: Adding validation in setter

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        print("Getting salary...")
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("Salary can't be negative!")
        else:
            print("Setting salary...")
            self._salary = new_salary

print("=== Example 3: Setter with Validation ===")
emp1 = Employee(5000)
print(emp1.salary)  # Output: 5000

# Try to set a negative salary
emp1.salary = -1000  # Output: Salary can't be negative!
print(emp1.salary)  # Output: 5000 (unchanged)

# Set a valid salary
emp1.salary = 6000
print(emp1.salary)  # Output: 6000

