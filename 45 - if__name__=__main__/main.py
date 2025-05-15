# main.py
# ============================
# 🧪 We are importing addition from addition.py
# ============================

import addition as ad  # Import the file and give it a short name (alias)

# Call the function from the imported file
function_call = ad.addition(20, 20)
print(function_call)

# ✅ Output after fixing with if __name__ == "__main__" in addition.py:
# calling addition function from addition.py file
# 40

# ❌ Without the if __name__ == "__main__" guard, the output would be:
# calling addition function from addition.py file   <- from imported file auto-run
# calling addition function from addition.py file   <- from this function call
# 40
