# ------------------------------------------------------------
# Multilevel Inheritance in Python
# ------------------------------------------------------------

# What is Multilevel Inheritance?
# ➤ In multilevel inheritance, a class is derived from a class that is also derived from another class.
#    Think: Grandparent → Parent → Child

# How to Use It?
# ➤ Just keep extending classes layer by layer.

# When to Use It?
# ➤ When classes are naturally dependent on each other in a hierarchy.

# Advantages:
# ✅ Inheritance flows in levels (easy to trace logic)
# ✅ Promotes code reusability across generations of classes
# ✅ Allows extending behavior step-by-step

# Disadvantages:
# ❌ Complex relationships can make debugging harder
# ❌ Changes in base class can affect all levels

# ------------------------------------------------------------
# Base Class (Grandparent)
# ------------------------------------------------------------
class World:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"Name of the world is {self.name}")

# ------------------------------------------------------------
# Intermediate Class (Parent)
# ------------------------------------------------------------
class Continent(World):
    def __init__(self, name, name_of_continent):
        super().__init__(name)  # Call World class constructor
        self.name_of_continent = name_of_continent

    def show_continent(self):
        print(f"Name of the continent is {self.name_of_continent}")

# ------------------------------------------------------------
# Derived Class (Child)
# ------------------------------------------------------------
class Country(Continent):
    def __init__(self, name, name_of_continent, country_name):
        super().__init__(name, name_of_continent)  # Call Continent class constructor
        self.country_name = country_name

    def get_details(self):
        print("➡ In multilevel inheritance class")
        print(f"Name of the country is {self.country_name}")
        
        # Calling parent and grandparent class methods
        self.show_continent()     # From Continent
        self.show_details()       # From World
        print("✅ Multilevel Inheritance Completed!")

# ------------------------------------------------------------
# Create Object and Test
# ------------------------------------------------------------
c = Country("Earth", "Asia", "Japan")
c.get_details()

# Output:
# ➡ In multilevel inheritance class
# Name of the country is Japan
# Name of the continent is Asia
# Name of the world is Earth
# ✅ Multilevel Inheritance Completed!
