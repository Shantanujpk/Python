# ✅ TUPLES IN PYTHON

# 🧠 What is a Tuple?
# A tuple is a collection that can store multiple values of different data types.
# BUT unlike lists, **tuples are immutable**, meaning you cannot change them after creation.

my_tuple = (1, 2, 3, 4, True, "Shan", 14.6, 'Ronaldo')
print("Type of my_tuple:", type(my_tuple), "\nTuple contents:", my_tuple)
# Output: <class 'tuple'> (1, 2, 3, 4, True, 'Shan', 14.6, 'Ronaldo')

# ------------------------------
# ⚠️ Common Confusion: Tuple with One Element

tuple1 = (1)
print("Type of tuple1:", type(tuple1), "\nValue:", tuple1)
# Output: <class 'int'> 1
# Because no comma is used, Python treats it as a number, NOT a tuple

# ✅ Correct Way to Create a Single-Element Tuple
tuple2 = (1,)
print("Type of tuple2:", type(tuple2), "\nValue:", tuple2)
# Output: <class 'tuple'> (1,)

# ------------------------------
# ❌ Tuples are IMMUTABLE
# You cannot change their values using indexing

# Uncommenting below will give an error
# my_tuple[1] = 80  
# TypeError: 'tuple' object does not support item assignment

# ------------------------------
# ✅ INDEXING IN TUPLES

# Accessing elements using positive indexing (starts from 0)
print("Element at index 0:", my_tuple[0])
print("Element at index 1:", my_tuple[1])
print("Element at index 2:", my_tuple[2])
print("Element at index 3:", my_tuple[3])

# ------------------------------
# ✅ NEGATIVE INDEXING
# Indexing from the end of the tuple using negative numbers

print("Element at index -4 (from the end):", my_tuple[-4])
# Explanation: Length is 8 → 8 - 4 = index 4 → Output: True

# ------------------------------
# ✅ MEMBERSHIP CHECK (Check if an element exists)

if 2 in my_tuple:
    print("✅ 2 is present in the tuple")
else:
    print("❌ 2 is NOT present")

if 200 in my_tuple:
    print("✅ 200 is present in the tuple")
else:
    print("❌ 200 is NOT present")

# ------------------------------
# ✅ SLICING TUPLES
# Syntax: tuple[start:stop:step]
# Tuples are immutable, so slicing returns a NEW tuple

print("Slice from index 1 to 2:", my_tuple[1:3])  # Index 1 and 2 only
print("Original tuple remains unchanged:", my_tuple)

# Store a slice in a new tuple
tuple3 = my_tuple[1:3]
print("New tuple (tuple3):", tuple3)

# ------------------------------
# ✅ SLICE WITH STEP/JUMP

# Every 2nd element from index 0 to 3 (exclusive)
print("Elements from 0 to 3 with step 2:", my_tuple[0:4:2])  # Output: (1, 3)

# From index 2 till the end
print("From index 2 to end:", my_tuple[2:])  # Output: (3, 4, True, 'Shan', 14.6, 'Ronaldo')

# From index 1 till the end
print("From index 1 to end:", my_tuple[1:])  # Output: (2, 3, 4, True, 'Shan', 14.6, 'Ronaldo')

# Every second (alternate) value from start to end
print("Every 2nd element from full tuple:", my_tuple[::2])  # Output: (1, 3, True, 14.6)
