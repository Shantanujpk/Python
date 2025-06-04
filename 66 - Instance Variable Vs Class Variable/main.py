"""🟡 Class Variables
Belong to the class itself, not to any one object (instance).

Shared by all instances of the class—if you change it in the class, it changes for everyone.

Used to store data that is common to all objects, like a counter for how many objects exist.

Defined outside any methods in the class.

🟠 Instance Variables
Belong to a specific object.

Unique for each instance—if you change it, it only affects that one object.

Used to store individual data for each object, like a name or score.

Usually defined inside the __init__ method (or other methods) using self.variable_name.

"""

# Python will first check if the instance variable is available for an instance if not it will use the class variable 

# 🟡 Creating a class called 'employee'
class employee:
    # 🟠 Class variables - shared by all instances of the class
    company_name = "Apple"
    companysize = 0

    # 🟡 Constructor - gets called every time you create a new employee
    def __init__(self, employeename):
        print("In constructor")  # This will print when an object is created

        # 🟠 Instance variable - specific to this object (employee)
        self.employeename = employeename

        # 🟠 Another instance variable
        self.raise_amount = 20

        # 🟠 Update class variable to track how many employees are created
        employee.companysize = employee.companysize + 1

    # 🟡 Method to show details about the employee
    def showdetails(self):
        # 🟠 self.company_name - first checks if there’s an instance variable.
        # If not found, it uses the class variable.
        print(
            f"Name of the employee is {self.employeename}, "
            f"size of the company is {employee.companysize}, "
            f"and name of the company is {self.company_name}."
        )

        # 🟠 Shows the raise amount for this employee
        print(f"{self.employeename} is getting a hike of {self.raise_amount}%.")


# 🟡 Creating the first employee object
emp1 = employee("Dan")
emp1.showdetails()  # Calls the showdetails method for emp1


# 🟡 Creating the second employee object
emp2 = employee("Adam")
emp2.showdetails()  # Calls the showdetails method for emp2


# 🟠 Checking if we can change the instance variable for emp1
print("\nChanging the instance variable (raise_amount) for Dan:")
emp1.raise_amount = 30  # Change raise_amount just for emp1
emp1.showdetails()  # Shows updated raise_amount for emp1

# 🟠 Checking if Adam's raise_amount has changed (it should NOT)
emp2.showdetails()  # Adam’s raise_amount remains 20


# 🟡 Checking if we can change the class variable (company_name) for emp2
print("\nChanging the class variable (company_name) for Adam to Google:")
emp2.company_name = "Google"  # This creates a NEW instance variable for emp2
emp2.showdetails()  # Now shows 'Google' for emp2

# 🟠 Checking if Dan’s company_name has changed (it should NOT)
print("\nChecking if Dan’s company_name changed:")
emp1.showdetails()  # Dan’s company_name remains 'Apple'

# 🟢 Explanation of why Adam’s change didn’t affect Dan:
# - company_name is a class variable shared by all instances.
# - BUT if you create an instance variable with the same name (like emp2.company_name),
#   it only affects that specific object.
# - So emp2 now has its own company_name = "Google" (instance variable),
#   while emp1 and the class still use the original class variable company_name = "Apple".
