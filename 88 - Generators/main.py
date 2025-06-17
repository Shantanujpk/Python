# --------------------------------------
# 🎯 Python Generators - Complete Guide
# --------------------------------------

# 🧠 What is a Generator?
# A generator is a special function that returns an iterator,
# which yields items one at a time, only when needed.

# ✅ HOW TO USE A GENERATOR FUNCTION

def count_up_to(max):
    """
    Generator function that yields numbers from 1 to max.
    """
    num = 1
    while num <= max:
        yield num  # Yield instead of return
        num += 1

print("\n📌 Generator Function Example:")
for number in count_up_to(5):
    print(number)


# ✅ GENERATOR EXPRESSION (Short-hand version of generator)

print("\n📌 Generator Expression Example:")
squares = (x * x for x in range(5))  # Note the use of () instead of []
for sq in squares:
    print(sq)


# ✅ ADVANTAGES OF GENERATORS

print("""
--------------------------------
✅ Advantages of Generators
--------------------------------
1. Memory Efficient - doesn't store the entire sequence.
2. Good for large datasets or infinite streams.
3. Lazy Evaluation - values are generated when needed.
""")

# ❌ DISADVANTAGES OF GENERATORS

print("""
--------------------------------
❌ Disadvantages of Generators
--------------------------------
1. One-time use - Once exhausted, can't reuse.
2. No indexing or slicing like lists.
3. Slightly harder to debug and test.
""")


# ✅ GENERATOR EXAMPLE: Fibonacci Sequence

def fibonacci():
    """
    Infinite Fibonacci generator.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n📌 First 10 Fibonacci Numbers using Generator:")
fib = fibonacci()
for _ in range(10):
    print(next(fib))


# ✅ COMPARISON: Generator vs List

print("""
-----------------------------------------
🔁 Generator vs List - Quick Comparison
-----------------------------------------
| Feature            | Generator  | List        |
|--------------------|------------|-------------|
| Memory Efficient   | ✅         | ❌          |
| Infinite Sequence  | ✅         | ❌          |
| Reusable           | ❌         | ✅          |
| Indexing Supported | ❌         | ✅          |
""")


# ✅ Generator with user input example

print("\n📌 Generator with user input - Stop at 'quit':")
def user_input_gen():
    while True:
        data = input("Enter something (or 'quit' to stop): ")
        if data == 'quit':
            break
        yield data

# Uncomment below to try it (VS Code or terminal)
# for item in user_input_gen():
#     print("You entered:", item)


# 📝 Summary:
# - Use generators for large data or memory-sensitive tasks.
# - Use `yield` instead of `return` in generator functions.
# - Combine with `next()` to manually fetch values.
# - Use generator expressions for compact code.

print("\n✅ Done! You now understand Python generators.")
