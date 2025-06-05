# 🟡 What is a class method?
# - It’s a method that works with the class itself, not just an instance.
# - It uses 'cls' as its first parameter (just like regular methods use 'self').
# - It can change class variables or perform operations related to the class.

# 🟠 Why use a class method?
# - To modify class variables that are shared by all instances.
# - To create alternative ways of making objects (like alternative constructors).
# - To keep code organized in the class if it’s related to the class (not to a single instance).

# 🟡 How to define and use a class method?
# - Use the @classmethod decorator.
# - Use 'cls' instead of 'self' to access class variables or create new instances.

class Employee:
    # 🟠 Class variable
    company = "Apple"

    def show(self):
        # 🟠 self.company checks if the instance has a company variable; if not, uses the class variable
        print(f"Name is {self.name} and company is {self.company}")

    # 🟠 Class method to change the class variable
    @classmethod
    def changeCompany(cls, new_name):
        # 🟠 cls refers to the class itself, not an object
        cls.company = new_name

# 🟡 Creating an object
e1 = Employee()
e1.name = "Lewis"

# 🟠 Show initial details
e1.show()  # Output: Name is Lewis and company is Apple

# 🟠 Changing the class variable using class method
# This updates the company name for the entire class (all current and future objects)
e1.changeCompany("Microsoft")

# 🟠 Show updated details
e1.show()  # Output: Name is Lewis and company is Microsoft

# 🟠 Summary:
# - @classmethod lets you change class variables.
# - All objects see the updated class variable.
# - This is useful for alternative constructors or any method that doesn’t rely on instance data.
