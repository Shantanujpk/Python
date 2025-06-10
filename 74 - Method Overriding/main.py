# 🧾 METHOD OVERRIDING IN PYTHON

# ------------------------------------------------------------------------------
# ❓ What is method overriding?
# ✅ Method overriding occurs when a child class provides its own implementation
#    of a method that is already defined in its parent class.
#    The method must have the same name and parameters.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ❓ Why use method overriding?
# ✅ To provide specific behavior in a subclass while reusing the structure of
#    the parent class. It allows customizing functionality for different types
#    of objects without changing the parent class.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# ❓ How to use method overriding?
# ✅ Define a method in the subclass with the same name as in the parent class.
#    Optionally, use `super()` to call the parent class’s version if needed.
# ------------------------------------------------------------------------------


# Base class: Shape
class Shape:
    def __init__(self, x, y):
        # Dimensions (used for rectangle by default)
        self.x = x
        self.y = y

    def area(self):
        # Generic area calculation (rectangle)
        return self.x * self.y


# Derived class: Circle (inherits from Shape)
class Circle(Shape):
    def __init__(self, r):
        self.r = r
        # Call parent constructor with r, r to fit the Shape structure
        super().__init__(r, r)

    def area(self):
        # ✅ Method Overriding: redefine area calculation for circle
        return 3.14 * self.r * self.r


# Derived class: Square (inherits from Shape)
class Square(Shape):
    def __init__(self, side):
        # Pass side as both x and y
        super().__init__(side, side)

    def area(self):
        # ✅ Method Overriding: redefine area calculation for square
        return self.x * self.x


# ---- USAGE EXAMPLES ----

# Rectangle using base class
rect = Shape(5, 10)
print("Rectangle Area:", rect.area())  # Output: 50

# Circle using overridden method
circle = Circle(7)
print("Circle Area:", circle.area())   # Output: 153.86

# Square using overridden method
square = Square(4)
print("Square Area:", square.area())   # Output: 16
