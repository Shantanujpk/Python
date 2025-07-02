"""📘 Problem Statement: Library Book Tracker using Python OOP
Objective:
Design a Python class named lib to simulate a simple library system that can:

Track and store a list of books assigned to each individual library object.

Maintain a cumulative count of all books added across multiple objects using class variables.

Store all book titles added across all objects in a shared list.

Automatically validate whether the number of books passed to each object matches the actual list length.

Provide a method to display object-specific book info, total books, and the full list of all books stored so far.

✅ Functional Requirements:
Each time a lib object is created, it should:

Accept a list of book titles.

Increment the global total book count.

Add the books to a global list shared across all instances.

Store the book list locally in the instance.

The class should include a checklen() method to:

Verify if the number of books for that instance matches the length of its book list.

Print the total number of books across all objects.

Display the entire book catalog from all instances.

🔧 Constraints:
Use Python OOP concepts like class variables and instance variables.

Do not allow any mismatch between the stated book count and actual list length without a validation alert."""

class lib:
    total_books = 0          # Class variable to count total books
    all_books = []           # Class variable to store all book names

    def __init__(self, books):
        self.books = books
        self.no_of_books = len(books)
        lib.total_books += self.no_of_books
        lib.all_books.extend(books)

    def checklen(self):
        print(f"\nChecking for this object...")
        print(f"Expected: {self.no_of_books}, Actual: {len(self.books)}")
        if self.no_of_books == len(self.books):
            print("✅ Book count is correct for this object.")
        else:
            print("❌ Book count mismatch in this object.")

        print(f"📚 Total books across all libraries: {lib.total_books}")
        print(f"🗂️ All books: {lib.all_books}")

b1 = lib(["Book A", "Book B"])
b1.checklen()

b2 = lib(["Book C", "Book D", "Book E"])
b2.checklen()

b3 = lib(["Book F"])
b3.checklen()

