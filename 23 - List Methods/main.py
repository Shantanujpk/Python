# ✅ Let's Learn About LIST METHODS in Python

# ℹ️ List is a collection of elements. Lists are *mutable*, meaning we can change them after creation.

my_list = [11, 12, 13, 14, 2, 4, 6, 7, 3, 6766, 34]

# ------------------------------
# 1️⃣ APPEND METHOD
# ➕ Adds an element to the END of the list
my_list.append(100)
print("After append:", my_list)
# Output: [11, 12, 13, 14, 2, 4, 6, 7, 3, 6766, 34, 100]

# ------------------------------
# 2️⃣ SORT METHOD (reverse=True)
# 🔁 Sorts the list in DESCENDING order
my_list.sort(reverse=True)
print("After sort (descending):", my_list)
# Output: [6766, 100, 34, 14, 13, 12, 11, 7, 6, 4, 3, 2]

# ------------------------------
# 3️⃣ INDEX METHOD
# 🔍 Finds the index (position) of the first occurrence of an element
index_of_12 = my_list.index(12)
print("Index of 12:", index_of_12)
# Output: 5
# Note: If 12 occurs more than once, it gives the index of the FIRST one.

# ------------------------------
# 4️⃣ COUNT METHOD
# 🔢 Counts how many times an element appears in the list
count_100 = my_list.count(100)
print("Count of 100:", count_100)
# Output: 1

# ------------------------------
# 5️⃣ COPY vs DIRECT ASSIGNMENT
# 📋 Let's understand the difference between = and .copy()

# 👉 Assignment using = (both variables point to the same list)
list2 = my_list
list2[0] = 999  # This will also change my_list
print("After modifying list2:", my_list)
# Output: [999, 100, 34, 14, 13, 12, 11, 7, 6, 4, 3, 2]

# ✅ To avoid changing the original list, use .copy()
list3 = my_list.copy()
list3[0] = 111  # This will NOT affect my_list
print("Original list after .copy():", my_list)
print("Copied list (list3):", list3)
# Output:
# my_list  → [999, 100, 34, 14, 13, 12, 11, 7, 6, 4, 3, 2]
# list3    → [111, 100, 34, 14, 13, 12, 11, 7, 6, 4, 3, 2]

# ------------------------------
# 6️⃣ INSERT METHOD
# 🧩 Inserts an element at a specific index

# ❌ This will REPLACE the value at index 1
list3[1] = 455
print("Replaced index 1 with 455:", list3)
# Output: [111, 455, 34, 14, 13, 12, 11, 7, 6, 4, 3, 2]

# ✅ To INSERT without replacing
my_list.insert(1, 455)
print("Inserted 455 at index 1:", my_list)
# Output: [999, 455, 100, 34, 14, 13, 12, 11, 7, 6, 4, 3, 2]

# ------------------------------
# 7️⃣ EXTEND METHOD
# ➕ Adds all elements of one list to the end of another

list4 = [2, 4, 6, 8, 10]
my_list.extend(list4)
print("After extending with list4:", my_list)
# Output: [999, 455, 100, 34, 14, 13, 12, 11, 7, 6, 4, 3, 2, 2, 4, 6, 8, 10]
# ⚠️ Note: This MODIFIES the original list (my_list)

# ------------------------------
# 8️⃣ CONCATENATION (using +)
# 🔗 Combines lists WITHOUT changing the original ones

list5 = list2 + list4
print("List 2 is:", list2)
print("List 4 is:", list4)
print("Concatenated List 5 (list2 + list4):", list5)
# Output: Combined list, while original lists stay unchanged
