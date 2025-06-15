# -----------------------------------------------------------
# 🛠️ Python shutil Module - Beginner-Friendly Guide
# -----------------------------------------------------------

# 📦 What is shutil?
# The shutil module provides functions for file and directory operations
# like copying, moving, deleting, and checking disk usage.

import shutil  # Import shutil for file operations
import os      # Import os for path and file handling

# -----------------------------------------------------------
# ✅ Step 1: Create Demo Directory and File
# -----------------------------------------------------------

print("🔧 Setting up demo files...")

# Create a demo folder called 'source_folder' if it doesn't exist
os.makedirs("source_folder", exist_ok=True)

# Create a file inside it
with open("source_folder/test_file.txt", "w") as f:
    f.write("This is a test file for shutil demonstration.")

print("✅ Created 'source_folder/test_file.txt'\n")

# -----------------------------------------------------------
# 📂 Step 2: Copy a File
# -----------------------------------------------------------

# Copy file to the current directory with a new name
shutil.copy("source_folder/test_file.txt", "copied_file.txt")
print("📂 Copied file to 'copied_file.txt'")

# -----------------------------------------------------------
# 📂 Step 3: Copy File with Metadata
# -----------------------------------------------------------

# This includes timestamps and permission bits
shutil.copy2("source_folder/test_file.txt", "copied_with_meta.txt")
print("📂 Copied file with metadata to 'copied_with_meta.txt'")

# -----------------------------------------------------------
# 📁 Step 4: Copy Entire Folder
# -----------------------------------------------------------

# Copy the whole source folder to 'backup_folder'
shutil.copytree("source_folder", "backup_folder", dirs_exist_ok=True)
print("📁 Copied folder to 'backup_folder'")

# -----------------------------------------------------------
# 🔁 Step 5: Move or Rename a File
# -----------------------------------------------------------

# Move/rename the copied file
shutil.move("copied_file.txt", "renamed_file.txt")
print("🔁 Moved 'copied_file.txt' to 'renamed_file.txt'")

# -----------------------------------------------------------
# ❌ Step 6: Delete Files and Folders
# -----------------------------------------------------------

# Delete the renamed file
os.remove("renamed_file.txt")
print("🗑️ Deleted 'renamed_file.txt'")

# Delete the copied folder
shutil.rmtree("backup_folder")
print("🗑️ Deleted 'backup_folder' and its contents")

# -----------------------------------------------------------
# 💾 Step 7: Get Disk Usage Info
# -----------------------------------------------------------

# Get disk usage statistics for current directory
total, used, free = shutil.disk_usage(".")

print("\n💾 Disk Usage Info:")
print(f"Total: {total // (1024**3)} GB")
print(f"Used : {used // (1024**3)} GB")
print(f"Free : {free // (1024**3)} GB")

# -----------------------------------------------------------
# 📝 Summary:
# - shutil.copy()        → Copy file
# - shutil.copy2()       → Copy file with metadata
# - shutil.copytree()    → Copy entire folder
# - shutil.move()        → Move or rename file/folder
# - shutil.rmtree()      → Delete folder recursively
# - shutil.disk_usage()  → Get storage stats
# -----------------------------------------------------------

print("\n✅ shutil demo complete!")
