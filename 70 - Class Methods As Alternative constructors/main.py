# 🟡 CLASS METHODS AS ALTERNATIVE CONSTRUCTORS

# 🔹 What is an alternative constructor?
# - It’s a different way to create an object of a class.
# - Sometimes you have data in a different format (like a string, dictionary, etc.)
# - A class method can process that data and return a new object.

# 🔹 Why use it?
# - To make object creation more flexible.
# - To separate logic for handling special input formats.

class Student:
    def __init__(self, name, marks):
        # 🟠 Standard constructor
        self.name = name
        self.marks = marks

    def show(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    # 🔹 Alternative constructor using @classmethod
    @classmethod
    def from_string(cls, student_str):
        # Takes a string like "John-88"
        name, marks = student_str.split("-")
        # Convert marks to integer and return new Student object
        return cls(name, int(marks))

# 🟢 Creating object using regular constructor
s1 = Student("Alice", 95)
s1.show()  # Output: Name: Alice, Marks: 95

# 🟢 Creating object using alternative constructor (from string)
s2 = Student.from_string("Bob-89")
s2.show()  # Output: Name: Bob, Marks: 89

# 🔹 Summary:
# - from_string() is a class method (notice the @classmethod decorator).
# - cls refers to the class itself (Student).
# - It parses a string and creates a new object.
# - This is useful when the input data isn’t in the regular (name, marks) format.
