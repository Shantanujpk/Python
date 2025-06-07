"""✅ What is super()?
In Python, super() is a built-in function that returns a proxy object, which allows you to refer to the parent class. It enables you to call methods and constructors from a parent class without explicitly naming it.

✅ Why use super()?
Code Reusability: Avoids redundancy by reusing methods from the parent class.

Maintainability: Facilitates easier updates and maintenance of code.

Multiple Inheritance Support: Ensures proper method resolution order (MRO) in complex inheritance hierarchies.

✅ How to use super()?
You can use super() to call methods from a parent class:"""

# Define the first parent class
class parentclass:
    def parent_method(self):
        print("this is the parent method")

# Define the second parent class
class parentclass1:
    def parent_method1(self):
        print("this is parent method from parent class 1")

# Define the child class inheriting from both parentclass and parentclass1
class childclass(parentclass, parentclass1):
    def childmethod(self):
        print("this is the child method")
        super().parent_method()   # Calls parent_method from parentclass
        super().parent_method1()  # Calls parent_method1 from parentclass1

# Create an instance of childclass
child_object = childclass()
child_object.childmethod()



class employee:
    def __init__(self,name, id, country, salary, age):
        self.name=name
        self.id=id
        self.country=country
        self.salary=salary
        self.age=age
        print("this is parent constructor")

class emp_skill_set(employee):
    def __init__(self,name, id, country, salary, age,skill):
        super().__init__(name, id, country, salary, age)
        self.skill = skill
        print("this is the child class function")
        
        

# Creating object of parent class
e1 = employee("Dan", 12, "USA", 20000, 25)

# Creating object of child class with skill
e11 = emp_skill_set("Adam", 13, "USA", 25000, 26, "Python")

# Accessing skill
print(f"Skill: {e11.skill}")
