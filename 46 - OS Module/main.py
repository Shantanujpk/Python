# ====================================================
# 📂 Python Tutorial: Using the `os` Module (Basics)
# ====================================================

# ✅ What is the `os` module?
# The `os` module in Python provides functions to interact with the operating system.
# It helps you work with files, directories, paths, environment variables, and more.

import os

# ----------------------------------------------------
# 🔍 1. Get current working directory
# ----------------------------------------------------
cwd = os.getcwd()  # Returns the current working directory
print("Current Working Directory:", cwd)

# ----------------------------------------------------
# 📁 2. List all files and folders in a directory
# ----------------------------------------------------
files = os.listdir()  # List items in the current directory
print("Files & Folders:", files)

# ----------------------------------------------------
# 📁 3. Create a new folder (directory)
# ----------------------------------------------------
# os.mkdir("test_folder")  # Creates a folder named 'test_folder'

# ----------------------------------------------------
# 🧹 4. Remove a folder (must be empty)
# ----------------------------------------------------
# os.rmdir("test_folder")  # Removes 'test_folder'

# ----------------------------------------------------
# 🔁 5. Change directory
# ----------------------------------------------------
# os.chdir("path/to/folder")  # Changes the current working directory

# ----------------------------------------------------
# 🧪 6. Check if a file or folder exists
# ----------------------------------------------------
print("Does 'data.csv' exist?", os.path.exists("data.csv"))
print("Is 'my_folder' a directory?", os.path.isdir("my_folder"))
print("Is 'script.py' a file?", os.path.isfile("script.py"))

# ----------------------------------------------------
# 🧬 7. Get environment variables (e.g., PATH)
# ----------------------------------------------------
env_path = os.environ.get('PATH')
print("System PATH:", env_path)

# ----------------------------------------------------
# 📌 8. Get file path components
# ----------------------------------------------------
file_path = os.path.join(os.getcwd(), "my_script.py")
print("Full file path:", file_path)

filename = os.path.basename(file_path)  # Gets the file name only
folder = os.path.dirname(file_path)     # Gets the folder name
print("Filename:", filename)
print("Folder:", folder)

# ----------------------------------------------------
# ✅ Summary of Common os Functions
# ----------------------------------------------------
# os.getcwd()            → Get current directory
# os.chdir(path)         → Change current directory
# os.listdir(path)       → List contents of directory
# os.mkdir(name)         → Create directory
# os.rmdir(name)         → Remove empty directory
# os.remove(file)        → Delete file
# os.path.exists(path)   → Check if path exists
# os.path.join()         → Safely join paths
# os.path.isfile(), os.path.isdir() → Check path type
# os.environ             → Access environment variables

# ----------------------------------------------------
# 🔚 Best Practices
# ----------------------------------------------------
# - Always check if a file or folder exists before deleting.
# - Use os.path.join() instead of manual path strings (especially for cross-platform compatibility).
# - Avoid hardcoding paths — use variables or config files.

