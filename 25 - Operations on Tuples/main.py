# ✅ TUPLE MANIPULATION IN PYTHON

# 🧠 Remember: Tuples are IMMUTABLE
# ❌ You cannot change them directly (like updating or adding elements)
# ✅ But you CAN convert a tuple to a list, modify it, and convert it back to a tuple

# ------------------------------
# Original Tuple
tuple1 = (1, 2, 3, 4, "USA", "INDIA")
print("Original Tuple:", tuple1)

# ------------------------------
# Step 1️⃣: Convert tuple to list (so we can modify it)
list_from_tuple = list(tuple1)
print("Converted to List:", list_from_tuple)
# Output: [1, 2, 3, 4, 'USA', 'INDIA']

# ------------------------------
# Step 2️⃣: Perform desired changes on the list

# ➕ Append a new element to the end of the list
list_from_tuple.append(30)

# ✏️ Change the value at index 1
list_from_tuple[1] = "Spain"

# ✅ Modified list
print("Modified List:", list_from_tuple)
# Output: [1, 'Spain', 3, 4, 'USA', 'INDIA', 30]

# ------------------------------
# Step 3️⃣: Convert the modified list back to a tuple
tuple_from_list = tuple(list_from_tuple)
print("New Tuple after changes:", tuple_from_list)
# Output: (1, 'Spain', 3, 4, 'USA', 'INDIA', 30)

# ✅ This is the only way to 'manipulate' a tuple: by converting it to a list and back


# ✅ CONCATENATING TUPLES IN PYTHON

# 🧠 Tuples are immutable, so any operation like addition (concatenation) creates a NEW tuple.
# 🧩 Original tuples remain unchanged.

# ------------------------------
# Define two tuples
tup = (1, 3, 5, 6, 3, 1, 3)
tup1 = ("shan", "dan")

# ➕ Concatenate tup and tup1
tup3 = tup + tup1

# ✅ This creates a new tuple (tup3), doesn't affect tup or tup1
print("New Concatenated Tuple:", tup3)
# Output: (1, 3, 5, 6, 3, 1, 3, 'shan', 'dan')

# 🧾 Original tuples are untouched
print("Original tup:", tup)
print("Original tup1:", tup1)

# ✅ TUPLE METHODS: count() and index()

# 📘 Let's work with this tuple:
tup = (1, 3, 5, 6, 3, 1, 3)

# ------------------------------
# 1️⃣ count()
# ➕ Used to count how many times a particular element occurs in a tuple

print("The count of 1 in tup is:", tup.count(1))
# Output: 2 (1 appears two times)

# ------------------------------
# 2️⃣ index()
# 🔍 Used to find the index (position) of the FIRST occurrence of an element

print("First occurrence of 1 is at index:", tup.index(1))
# Output: 0 (the first 1 appears at index 0)

# ------------------------------
# 3️⃣ index() with start and end
# 📌 Syntax: tuple.index(element, start, end)
# - start: the index to start searching from (inclusive)
# - end: the index to stop searching (exclusive)

# ✅ Let’s find the index of 1, starting from index 1:
print("Index of 1 starting from index 1:", tup.index(1, 1))
# Output: 5 (the next 1 appears at index 5)

# ⚠️ Invalid example that raises an error:
# print(tup.index(1, 6, 2))
# ❌ This will raise a ValueError because:
# - The search range is from index 6 to 2 (which is an invalid range, as start > end)
# - Also, `index()` does not support a "jump" (step) parameter like slicing

# So, remove the third parameter (jump) — it's not valid for `index()`!

# 🔁 Reminder: If the value is not found within the range, it raises a ValueError
try:
    print("Trying index of 1 from index 6 to 2 (invalid):", tup.index(1, 6, 2))
except ValueError as e:
    print("Error:", e)