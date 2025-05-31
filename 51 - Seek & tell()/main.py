"""📌 What is .seek()?
.seek() is a file object method in Python that allows you to move the file pointer to a specific position within a file.

📌 Why do we use it?
When reading or writing to a file, .seek() lets you jump to a specific position rather than just reading from start to end.

For example, if you want to re-read a portion of a file or skip a header, .seek() helps you control where the reading/writing begins.

📌 How helpful is it?
✅ It improves flexibility: You’re not stuck with linear file reading—jump to where you need data!
✅ It supports more complex file operations: Re-read or update specific file sections without reopening.
✅ It’s essential for binary file handling (like images or audio), where data is accessed in chunks."""


with open('file.txt','r') as f:
    print(type(f))
    f.seek(10) # move to the 10th byte of the file
    print("Seek")
    data = f.read(5) # This will read the next 5 bytes
    print(data) 


"""📌 What is .tell()?
.tell() is a file object method in Python that returns the current position of the file pointer (as an offset in bytes) from the beginning of the file.

📌 Why do we use it?
It helps you track where you are in a file.

If you’re reading or writing data in chunks, .tell() can confirm your position, which is important for precise file handling or debugging.

📌 How helpful is it?
✅ It provides clarity: Knowing exactly where you are in a file helps avoid confusion when reading or writing.
✅ It’s useful for validation: After seeking or partial reads, you can confirm that the pointer is in the expected position.
✅ It aids in error handling and file manipulation by giving precise control over file operations."""


with open('file.txt','r') as f:
    print(type(f))
    f.seek(12) # move to the 10th byte of the file
    print("Tell")
    print(f.tell())
    data1 = f.read(5) # This will read the next 5 bytes
    print(data) 



"""📌 What is .truncate()?
.truncate() is a file object method in Python that resizes the file to a specified size (in bytes).

If no size is provided, it truncates the file to the current file pointer position.

📌 Why do we use it?
To shorten a file by removing data beyond a certain point.

It’s handy when you want to erase unwanted data or reset a file’s content.

📌 How helpful is it?
✅ It gives you control over file size and lets you remove data you no longer need.
✅ Useful for resetting temporary files or logs during a program’s execution.
✅ Helps manage disk space by removing unneeded parts of a file.
"""

with open('sample.txt','w') as s:
    s.write("abcdefghijklmnopqrstuvwxyz")
    s.truncate(10) # will cut the file details after 10th position

with open('sample.txt','r') as r:
    print(r.read())



