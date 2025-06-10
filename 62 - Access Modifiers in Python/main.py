# Access modifiers
# In Python:
# - public: accessible everywhere
# - protected: accessible within the class and its subclasses (convention with a single underscore _)
# - private: accessible only within the class (double underscore __)
# -  Encapsulation is the concept of wrapping data (variables) and methods (functions) into a single unit — typically a class — and restricting direct access to some of the object's components.
class Company:
    def __init__(self, age, name):
        self.age = age           # public
        self.name = name         # public

e = Company(12, "TCS")
print(e.age)
print(e.name)

class Employee:
    def __init__(self, name, department):
        self._department = department  # protected
        self.__name = name             # private

    def show_details(self):
        print(f"Name: {self.__name}, Department: {self._department}")

a = Employee("Harsh", "IT")

# Accessing protected attribute directly (still accessible but not recommended)
print(a._department)  # Output: IT

# Accessing private attribute directly (will raise error)
# print(a.__name)  # Uncommenting this will cause error

# Accessing private attribute indirectly
print(a._Employee__name)  # Output: Harsh

# Using method to show details
a.show_details()  # Output: Name: Harsh, Department: IT
