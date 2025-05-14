# ==============================
# 📘 Learn enumerate() in Python
# ==============================

# -----------------------------
# ❓ What is enumerate()?
# -----------------------------
# The enumerate() function adds a counter (index) to an iterable
# like a list, string, or tuple and returns it as an enumerate object.
# It lets you loop over both index and value in a single step.

# -----------------------------
# ✅ Why is enumerate() useful?
# -----------------------------
# - You don't need to manually declare and increment an index variable.
# - It makes code cleaner, shorter, and easier to read.
# - Works with lists, strings, tuples, sets, and other iterables.

# -----------------------------
# 👍 Advantages of enumerate()
# -----------------------------
# - Simplifies loops where index is needed
# - Cleaner syntax than using range(len(...))
# - Avoids indexing bugs

# -----------------------------
# 👎 Disadvantages
# -----------------------------
# - Not useful if you don’t need the index at all
# - Beginners might find syntax unfamiliar at first

# -----------------------------
# 🔒 Best Practices
# -----------------------------
# - Use when both index and value are required in a loop
# - Avoid range(len(...)) where possible for readability
# - Use descriptive variable names for index and value

# -----------------------------
# 🚀 Let's look at examples now!
# -----------------------------

# ========== Example 1: Without enumerate (Manual Check for Value) ==========
marks = [1, 2, 4, 5, 85, 632, 142, 56, 22, 101, 1]  # Student marks out of 1000

print("=== Without Enumerate and with known value ===")

# Loop through each mark
for mark in marks:
    print("Mark is:", mark)  # Print current mark
    if mark == 632:  # If the mark is 632 (we already know the value)
        print("Amazing !! You are the topper of the exam !! Keep it up")

print("Out of for loop!\n")


# ========== Example 2: Without enumerate (Using Manual Index) ==========
print("=== Without Enumerate and with known index ===")

index = 0  # Start a manual index
for mark in marks:
    print("Mark is:", mark)  # Print current mark
    if index == 5:  # We know the topper is at index 5
        print("Amazing !! You are the topper of the exam !! Keep it up")
    index += 1  # Manually increment index

print("Out of for loop of Index!!!\n")


# ========== Example 3: Using enumerate() ==========
print("=== Using Enumerate ===")

# Using enumerate() to get both index and mark
for index, mark in enumerate(marks):
    print("Index is:", index)  # Print current index
    if index == 5:  # Check if it's the 5th index
        print(mark, ", Amazing !! You are the topper of the exam !! Keep it up")

print("Out of for loop with enumerate!\n")


# ========== Example 4: Using enumerate() with Strings ==========
print("=== Enumerate on a String ===")

name = "Dan Williams"  # String variable

# Loop through string using enumerate()
for s_index, n in enumerate(name):
    print("Index for", n, "is", s_index)  # Print character and its index
    if s_index == 4:  # Check specific index
        print("W is not acceptable\n")  # Message when 'W' is found


# ========== Example 5: Using enumerate() with Tuples ==========
print("=== Enumerate on a Tuple ===")

tuple_enum = ("Dan", 45, "NY", "USA", 45441145)  # Tuple with different types

# Loop through tuple using enumerate()
for t_index, tu in enumerate(tuple_enum):
    print("Index for tuple element is", t_index)  # Print index
    if t_index == 3:  # Check specific index
        print("Country not allowed\n")  # Print warning


# ========== Example 6: Using enumerate() with custom start ==========
print("=== Enumerate with custom start index ===")

# Start counting from 1 instead of default 0
for i, mark in enumerate(marks, start=1):
    print("Student", i, "scored", mark)  # Print student number and mark
