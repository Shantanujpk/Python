# ---------------------------------------------------
# 🦦 Walrus Operator (:=) in Python - Beginner Guide
# ---------------------------------------------------

# What is Walrus Operator?
# ➤ Introduced in Python 3.8.
# ➤ Allows assignment AND usage of a variable in a single expression.
# ➤ Syntax: variable := expression

# ---------------------------------------------------
# ✅ Example 1: Normal assignment vs walrus assignment
t = True
print("Standard assignment:", t)

# Using walrus operator to assign and print in one line
print("Walrus assignment:", (f := False))  # Assigns False to f and prints it

# ---------------------------------------------------
# ✅ Example 2: While loop without walrus operator
print("\nWhile loop without walrus:")
l = [1, 2, 3, 4, 5, 6]
while len(l) > 0:
    print(l.pop())

# ---------------------------------------------------
# ✅ Example 3: While loop with walrus operator
print("\nWhile loop with walrus:")
l2 = [1, 2, 3, 4, 5, 6, 7]

# Important: Parentheses are required around (n := len(l2)) > 0
while (n := len(l2)) > 0:
    print(f"Popped from list (remaining {n} items):", l2.pop())

# ---------------------------------------------------
# ✅ Example 4: Getting user input in loop (without walrus)
print("\nCollecting fruits (without walrus):")
l3 = []
while True:
    i = input("Enter a fruit you like (or type 'quit' to stop): ")
    if i == 'quit':
        break
    l3.append(i)
print("Fruits list:", l3)

# ---------------------------------------------------
# ✅ Example 5: Getting user input in loop (with walrus)
print("\nCollecting animals (with walrus):")
l4 = []
while (animal := input("Enter an animal you like (or type 'quit' to stop): ")) != 'quit':
    l4.append(animal)
print("Animals list:", l4)

# ---------------------------------------------------
# ✅ Advantages of Walrus Operator:
# - Cleaner and more concise code.
# - Avoids repeating expressions.
# - Useful in loops, list comprehensions, and conditionals.

# ❌ Disadvantages:
# - Can reduce readability if overused or used in complex expressions.
# - Only supported in Python 3.8 and above.

# ---------------------------------------------------
# Summary:
# Use walrus operator `:=` when you want to:
# - Assign and use a value **at the same time**
# - Especially useful in **loops** and **conditions**
# ---------------------------------------------------
