# ====================================================
# 🌐 Python Tutorial: Local vs Global Variables
# ====================================================

# ----------------------------------------------------
# ✅ What is a Local Variable?
# A variable declared inside a function.
# It's only accessible within that function.
# ----------------------------------------------------

# ✅ What is a Global Variable?
# A variable declared outside all functions.
# It can be accessed inside and outside of functions.
# Its value stays the same unless explicitly modified using the 'global' keyword.
# ----------------------------------------------------

# Global variable
x = 10
print("🔹 Global variable before function call:", x)

def global_local_variable():
    print("\n📍 Inside the function:")
    
    # Local variable: only exists inside this function
    y = 10
    print(f"Local variable y = {y}")
    
    # Use 'global' keyword to modify the global variable x
    global x
    x = 15
    print(f"Modified global variable x inside function = {x}")

# Call the function
global_local_variable()

# Global variable value after the function call
print("\n🔹 Global variable after function call:", x)

# ----------------------------------------------------
# 📝 Notes:
# - Without using the `global` keyword, assigning x = 15 inside the function
#   would create a new local variable named x, leaving the global x unchanged.
# - Using `global x` tells Python: "I'm referring to the global variable x."
# ----------------------------------------------------

# ✅ OUTPUT:
# 🔹 Global variable before function call: 10
# 📍 Inside the function:
# Local variable y = 10
# Modified global variable x inside function = 15
# 🔹 Global variable after function call: 15
