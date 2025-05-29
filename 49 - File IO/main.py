# ====================================================
# 📂 Python Tutorial: File Handling (Basics) : Important if you want to save any data from program in a file etc ..
# ====================================================

# 📝 Python has built-in methods for reading, writing, and modifying files.
# These are used for working with text files (.txt), CSVs, logs, and more.

# ----------------------------------------------------
# ✅ Opening a File
# Use open("filename", mode)
# Modes:
# "r" → read (default)
# "w" → write (overwrite)
# "a" → append
# "x" → create new file
# "b" → binary mode
# ----------------------------------------------------

# Let's create a text file and write to it

# Writing to a file (creates if not exists, overwrites if exists)
with open("sample.txt", "w") as file:
    file.write("Hello! This is the first line.\n")
    file.write("This is the second line.\n")

print("✅ File written successfully.")

# ----------------------------------------------------
# 📖 Reading a File
# ----------------------------------------------------
with open("sample.txt", "r") as file:
    content = file.read()
    print("\n📄 File content:\n", content)

# ----------------------------------------------------
# 📚 Reading line by line
# ----------------------------------------------------
with open("sample.txt", "r") as file:
    print("🔹 Reading line by line:")
    for line in file:
        print(line.strip())  # .strip() removes newline characters

# ----------------------------------------------------
# ✏️ Appending to a File
# ----------------------------------------------------
with open("sample.txt", "a") as file:
    file.write("This line was added later.\n")

print("\n✅ Line appended.")

# ----------------------------------------------------
# 🧹 Best Practices
# ----------------------------------------------------
# - Use `with open(...)` → automatically closes the file
# - Always handle exceptions using try-except for critical file operations
# - Avoid hardcoding file paths (use os.path.join for portability)

# ----------------------------------------------------
# ❌ Deleting a File (optional)
# ----------------------------------------------------
# import os
# if os.path.exists("sample.txt"):
#     os.remove("sample.txt")
#     print("🗑️ sample.txt deleted.")
# else:
#     print("❌ File does not exist.")

# ----------------------------------------------------
# 🧠 Summary
# open() → Open the file
# read(), readline(), readlines() → Read data
# write(), writelines() → Write data
# with open(...) → Recommended method (auto-close)
# os.remove() → Delete a file
