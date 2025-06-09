# ------------------------------
# Single Inheritance in Python
# ------------------------------

# What is Single Inheritance?
# ➤ It is when a child class inherits from only one parent class.

# Advantages:
# ✅ Code reuse
# ✅ Simple and easy to understand
# ✅ Supports polymorphism

# Disadvantages:
# ❌ Limited to one parent
# ❌ Can cause tight coupling
# ❌ May require code duplication if other unrelated classes need similar functionality

# --------------------------------
# Parent Class: Animal
# --------------------------------
class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def makesound(self):
        print("Animal sound")  # Default sound

# --------------------------------
# Child Class: Dog (Single Inheritance from Animal)
# --------------------------------
class Dog(Animal):
    def __init__(self, name, breed):
        # super() calls the constructor of the parent class (Animal)
        super().__init__(name, breed)

    def makesound(self):
        # Overriding parent method
        print("Bark")

# --------------------------------
# Child Class: Cat (Single Inheritance from Animal)
# --------------------------------
class Cat(Animal):
    def __init__(self, name, breed):
        # Reusing Animal class constructor
        super().__init__(name, breed)

    def makesound(self):
        # Overriding parent method
        print("Meow")

# --------------------------------
# Creating Objects and Calling Methods
# --------------------------------

# Object of parent class
a = Animal("Dog", "Golden Retriever")
a.makesound()  # Output: Animal sound

# Object of child class Dog
b = Dog("Dog", "Doberman")
b.makesound()  # Output: Bark

# Object of child class Cat
c = Cat("Cat", "Indian")
c.makesound()  # Output: Meow
