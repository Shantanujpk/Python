# 🔁 1. union()
# Combines elements from both sets (removes duplicates), returns a new set
a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print("Union:", c)  # {1, 2, 3, 4, 5}

# 🔁 2. update()
# Adds elements from b to a, modifies a in-place
a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)
print("Update (union update):", a)  # {1, 2, 3, 4, 5}


# 🤝 3. intersection()
# Returns only the common elements between sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
print("Intersection:", c)  # {3, 4}

# 🤝 4. intersection_update()
# Keeps only common elements in the original set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.intersection_update(b)
print("Intersection Update:", a)  # {3, 4}


# 🔄 5. symmetric_difference()
# Returns elements that are in either set but not in both
a = {1, 2, 3}
b = {3, 4, 5}
c = a.symmetric_difference(b)
print("Symmetric Difference:", c)  # {1, 2, 4, 5}

# 🔄 6. difference()
# Returns elements that are only in set a (a - b)
a = {1, 2, 3, 4}
b = {3, 4, 5}
c = a.difference(b)
print("Difference (a - b):", c)  # {1, 2}

# 🔄 7. difference_update()
# Removes elements found in another set from the original set
a = {1, 2, 3, 4}
b = {3, 4, 5}
a.difference_update(b)
print("Difference Update (a - b):", a)  # {1, 2}


# 📌 INBUILT SET METHODS

# 🔍 isdisjoint()
# Returns True if sets have no common elements
a = {1, 2, 3}
b = {4, 5, 6}
print("Is Disjoint:", a.isdisjoint(b))  # True

# 🔍 issubset()
# Returns True if all elements of set a are in b
a = {1, 2}
b = {1, 2, 3, 4}
print("Is Subset:", a.issubset(b))  # True

# 🔍 issuperset()
# Returns True if set a has all elements of b
a = {1, 2, 3, 4}
b = {2, 3}
print("Is Superset:", a.issuperset(b))  # True


# 🧱 add()
# Adds a single element to the set
a = {1, 2, 3}
a.add(4)
print("Add:", a)  # {1, 2, 3, 4}

# 🧱 update()
# Adds multiple elements (can use list, tuple, set)
a = {1, 2}
a.update([3, 4], (5, 6))
print("Update with multiple:", a)  # {1, 2, 3, 4, 5, 6}

# ❌ remove()
# Removes an element; raises KeyError if not found
a = {1, 2, 3}
a.remove(2)
print("Remove:", a)  # {1, 3}

# 🚫 discard()
# Removes an element; does NOT raise error if not found
a = {1, 2, 3}
a.discard(4)  # No error even though 4 not in set
print("Discard:", a)  # {1, 2, 3}

# 🧺 pop()
# Removes and returns a random element
a = {10, 20, 30}
removed = a.pop()
print("Popped:", removed)
print("After Pop:", a)

# 🧹 clear()
# Removes all elements from the set
a = {1, 2, 3}
a.clear()
print("After Clear:", a)  # set()

# 🧨 del
# Deletes the set entirely
a = {1, 2, 3}
del a
# print(a)  # This will cause NameError: name 'a' is not defined
