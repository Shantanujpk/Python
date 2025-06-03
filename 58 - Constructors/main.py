# -------------------------------------------------------------------
# 📝 What is a Constructor?
# - A constructor is a special method in a class that gets called 
#   automatically when you create (instantiate) an object of that class.
# - In Python, the constructor is always named __init__().
# - Constructors can help set up initial values or perform startup actions.

# 📝 Types of Constructors:
# 1️⃣ Default Constructor: Takes only 'self' (no extra parameters)
# 2️⃣ Parameterized Constructor: Takes 'self' + extra parameters

# -------------------------------------------------------------------
# 🐍 Example 1: Default Constructor
class Customer:
    # This is a default constructor because it only takes 'self'
    def __init__(self):
        # This message will print automatically when you create a Customer object
        print("Yoo !! I am a constructor which is defined in the Customer class.")
        print("I get called automatically when you create a Customer object.")
        print("And I always return None (in Python constructors return None by default).")
        print("In this case, I am a default constructor because you haven't passed any arguments other than self.")

    # Class attributes
    name = "Dan"
    occupation = "CEO"

    # Method to display information about the customer
    def info(self):
        print(f"My name is {self.name} and I am {self.occupation} !!")

# -------------------------------------------------------------------
# 🎯 Creating an object of the Customer class
# This will automatically call the default constructor (__init__)
a = Customer()

# -------------------------------------------------------------------
# 🐍 Example 2: Parameterized Constructor
class Company:
    # This is a parameterized constructor because it takes extra arguments: name and location
    def __init__(self, name, location):
        # Prints information as soon as an object is created
        print("Yoo !! I am a constructor which is defined in the Company class.")
        print("I get called automatically when you create a Company object.")
        print("And I always return None.")
        print("In this case, I am a parameterized constructor because you passed additional arguments (name, location).")
        print(f"The company name is {name} and it is located in {location}!!")

    # Class attributes (will be used only if not overridden in the constructor)
    name = "Amazon"
    location = "WA, USA"

    # Method to display information
    def info(self):
        print("I will be called if you assign the class Company to an object and then call info() without passing parameters.")
        print(f"The company name is {self.name} and it is located in {self.location}!!")

# -------------------------------------------------------------------
# 🎯 Creating an object of the Company class with parameters
print("\n")
b = Company("JP Morgan", "New York")  # This will call the parameterized constructor

# 🎯 Calling the info() method
print(b.info())  # This will use the class attributes defined in the class, not the constructor

# -------------------------------------------------------------------
# 💡 My Favorite Part
# Constructors are like the welcoming committee of a class. 
# They set things up and make sure everything’s in place before you start using the object! 🚀
# In Python, you don’t have to remember to “call” them — they jump into action automatically!

