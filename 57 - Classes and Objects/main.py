# --------------------
# Introduction to Classes, Objects and self keyword
# --------------------

# A class is a blueprint or template to create objects
class person_details:
    # These are **class attributes** (shared by all objects, unless changed)
    Name = 'Carlos'
    Sirname = 'Sainz'
    Occupation = 'F1 Driver'
    Account = 100000

    # 'self' refers to the current object
    def info(self):
        # Access data of the object using self
        print(f"The candidate name is {self.Name} and occupation is {self.Occupation}")

# Create an object 'a' from the class 'person_details'
a = person_details()
print(a.Name)         # prints: Carlos
a.info()              # prints: The candidate name is Carlos and occupation is F1 Driver

# We can do it for multiple objects without needing to write the same code
b = person_details()
b.Name = "Lewis"      # Overriding the default Name for this object
b.Sirname = "Hamilton"
b.Occupation = "F1 Coach"
b.info()              # prints: The candidate name is Lewis and occupation is F1 Coach


# --------------------
# Additional explanation for beginners:
# --------------------

# In Python:
# ✅ Class: like a recipe (blueprint).
# ✅ Object: the actual thing you make (like a real cookie).
# ✅ self: points to the current object.
# ✅ Class attributes: shared by all objects, but can be overridden.

# self example:
# - When you call 'a.info()', Python automatically passes 'a' as 'self'.
# - Inside the 'info' function, 'self' lets you access that specific object's data.

# That’s why you see:
# self.Name --> a.Name or b.Name
# self.Occupation --> a.Occupation or b.Occupation

# OOP is great because you can create multiple objects from one class
# and customize each one separately!

