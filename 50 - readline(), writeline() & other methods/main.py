# ====================================================
# 📘 Python File Reading Methods: read(), readline(), readlines()
# ====================================================

# First, let’s write a sample file to work with
with open("example.txt", "w") as file:
    file.write("Line 1: Hello, Python!\n")
    file.write("Line 2: File handling is useful.\n")
    file.write("Line 3: We are learning read methods.\n")

# ----------------------------------------------------
# 1️⃣ read() – Reads the entire file as a single string
# ----------------------------------------------------
with open("example.txt", "r") as file:
    content = file.read()
    print("🔹 Using read():")
    print(content)

# ----------------------------------------------------
# 2️⃣ readline() – Reads one line at a time
# ----------------------------------------------------
with open("example.txt", "r") as file:
    print("🔹 Using readline():")
    line1 = file.readline()
    print("First line:", line1.strip())

    line2 = file.readline()
    print("Second line:", line2.strip())

# ----------------------------------------------------
# 3️⃣ readlines() – Reads all lines into a list
# ----------------------------------------------------
with open("example.txt", "r") as file:
    print("🔹 Using readlines():")
    lines = file.readlines()
    print("All lines as a list:", lines)
    for idx, line in enumerate(lines):
        print(f"Line {idx + 1}: {line.strip()}")

# ----------------------------------------------------
# 🧠 Summary of Methods
# ----------------------------------------------------
# read()      → Returns full content as one string
# readline()  → Returns the next line each time it's called
# readlines() → Returns all lines as a list of strings

# ----------------------------------------------------
# 🧹 Best Practice
# Always use 'with open(...)' to auto-close the file
