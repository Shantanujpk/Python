# 🟡 What is a static method?
# - It belongs to the class, not to any specific object (instance).
# - It doesn’t use self or cls because it doesn’t need the instance or class itself.
# - It’s defined using the @staticmethod decorator.
# - We keep it inside the class so that whoever uses the class can also use this extra helper method.

# 🟠 Let’s create a simple example:

class Science:
    def __init__(self, marks):
        self.marks = marks  # Instance variable (specific to each object)

    # A regular method - uses self because it works with instance variables
    def show_marks(self):
        print(f"Total marks out of 100 are {self.marks}")

    # A static method - does NOT use self or cls, just a normal method inside the class
    @staticmethod
    def bonus_marks(marks, bonus):
        print(f"Adding Bonus {bonus} to {marks}: {marks + bonus}")

# 🟣 Let’s create an object (instance) of the Science class
student1 = Science(50)

# Calling the regular method
student1.show_marks()  # Output: Total marks out of 100 are 50

# 🟢 How to call the static method?
# Option 1: Using the instance (student1)
student1.bonus_marks(50, 10)  # Output: Adding Bonus 10 to 50: 60

# Option 2: Using the class itself
Science.bonus_marks(30, 20)   # Output: Adding Bonus 20 to 30: 50

# 🟤 Why use static methods?
# - When you have a function that doesn’t need to know anything about the instance (self) or the class (cls).
# - But you still want to keep it in the class because it’s related to the class and useful for anyone using it.

# 🟡 Example: bonus_marks doesn’t care about self.marks – it just adds two numbers and helps whoever uses this class!
