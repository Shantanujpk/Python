# =========================================================
# 🔍 Understanding: if __name__ == "__main__"
# =========================================================

# ✅ What is it?
# ----------------
# It's a conditional block used to control what code runs when a file
# is either:
#   a) Run directly → executes the block
#   b) Imported into another file → does NOT execute the block

# ✅ Why use it?
# ----------------
# To make sure test/demo code doesn't run when the file is imported.

# =========================================================
# ✅ Advantages of using: if __name__ == "__main__"
# =========================================================

# 1️⃣ Prevents unwanted execution
#     - Only runs when the script is executed directly
#     - Avoids running code when imported

# 2️⃣ Cleaner imports
#     - Doesn't execute print() or function calls on import
#     - Keeps module behavior predictable

# 3️⃣ Modular design
#     - Encourages writing reusable and testable code

# 4️⃣ Testing-ready
#     - Lets you test functions inside the file directly

# 5️⃣ Good structure
#     - Separates reusable logic (functions, classes) from execution logic

# =========================================================
# ❌ Disadvantages of using: if __name__ == "__main__"
# =========================================================

# 1️⃣ Confusing for beginners
#     - New users might wonder why some code "isn't running"

# 2️⃣ Can lead to messy test code
#     - If used for large demos/test code, the file can get cluttered

# 3️⃣ Not enforced
#     - Python still allows top-level code outside this block,
#       which can cause accidental execution on import

# 4️⃣ Less relevant in some frameworks
#     - Web apps (like Flask/Django) often have separate run managers

# =========================================================
# 💡 Example
# =========================================================

def addition(a, b):
    return a + b

# This block will only run if this file is run directly
# NOT when it is imported from another file
if __name__ == "__main__":
    result = addition(10, 5)
    print("Result of addition is:", result)

# If this file is imported into another Python file like:
#     import filename
# The addition(10, 5) will NOT run. Only the function will be available.

# =========================================================
# 📦 Summary:
# Use this when you want to:
# - Reuse your file as a module
# - Add test/demo code that shouldn't run on import
