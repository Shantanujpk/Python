# import os

# def rename(filename):
#     number = 0
#     source = f'clutter/{filename}'
#     destination = f'clutter/{number}.png'
#     print(destination)

#     print(f"Source path: {source}")
#     print(f"Destination path: {destination}")

#     if not os.path.exists(source):
#         print("Error: Source file does not exist.")
#         return

#     if os.path.exists(destination):
#         print("Error: Destination file already exists.")
#         filename = destination
#         basename = os.path.basename(filename)      # '0.png'
#         number_str = os.path.splitext(basename)[0] # '0'
#         number = int(number_str)  
#         number= number + 1
#         destination = f'clutter/{number}.png'
#         os.rename(source, destination)
#         return destination
#     print("1")
#     os.rename(source, destination)
#     print("File renamed successfully.")
    

# f = 'shantanu.sa'
# rename(f)

# # 2.png 
# # or 
# # lasfile+1 


import os

def rename(filename):
    number = 0
    source = f'clutter/{filename}'

    print(f"Source path: {source}")

    if not os.path.exists(source):
        print("Error: Source file does not exist.")
        return

    # Loop until a destination filename doesn't exist
    while True:
        destination = f'clutter/{number}.png'
        print(f"Trying destination: {destination}")
        if not os.path.exists(destination):
            break
        number += 1

    os.rename(source, destination)
    print(f"File renamed successfully to {destination}")
    return destination

# Example calls
rename('shantanu.sa')
rename('anotherfile.txt')
rename('thirdfile.pdf')
