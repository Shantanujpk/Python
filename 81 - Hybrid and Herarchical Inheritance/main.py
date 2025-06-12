# ---------------------------------------------
# Hierarchical Inheritance in Python
# ---------------------------------------------

# What is Hierarchical Inheritance?
# ➤ One parent class with multiple child classes.

# Base class
class Animal:
    def sound(self):
        print("Animals make different sounds")

# Child class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating objects of child classes
dog = Dog()
cat = Cat()

print("Hierarchical Inheritance Output:")
dog.sound()  # Output: Dog barks
cat.sound()  # Output: Cat meows

print("\n---------------------------------------------\n")

# ---------------------------------------------
# Hybrid Inheritance in Python
# ---------------------------------------------

# What is Hybrid Inheritance?
# ➤ Combination of two or more types of inheritance (like hierarchical + multiple)

# Base class
class Person:
    def info(self):
        print("I am a person")

# Child class 1 (inherits from Person)
class Student(Person):
    def role(self):
        print("I am a student")

# Child class 2 (inherits from Person)
class Employee(Person):
    def role(self):
        print("I am an employee")

# Hybrid class (inherits from both Student and Employee)
class Intern(Student, Employee):
    def intern_info(self):
        print("I am an intern")

# Creating object of hybrid class
intern = Intern()

print("Hybrid Inheritance Output:")
intern.info()         # Inherited from Person (via MRO)
intern.role()         # MRO will choose Student.role() first
intern.intern_info()  # Defined in Intern class

# Checking method resolution order
print("\nMethod Resolution Order (MRO):")
print(Intern.mro())  # Shows the order Python will search for methods
