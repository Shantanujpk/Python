# What is finally? 
# A block of code that will always execute no matter what happens:
# - if an error occurs
# - if the program fails
# - or if the program runs successfully
# BUT there’s a catch... let’s see 👇

# Let's say I want a value from a dictionary using user input,
# and I give the wrong value (like a string instead of an integer)

dic = {1: 5, 2: 7, 3: 9}
x = input("Enter key: ")

# Try converting the input to integer and accessing the dictionary
try:
    key = int(x)
    # Check if the key exists in the dictionary
    if key in dic:
        print("Value for entered key is:", dic[key])
    else:
        print("Wrong input")
except:
    print("Value you have entered is wrong. Make sure it is an integer.")
finally:
    print("I will execute no matter what")  # ✅ This will run no matter what

'''
Example Output:
Enter key: a
Value you have entered is wrong. Make sure it is an integer.
I will execute no matter what
'''

"""
Example Output:
Enter key: 1
Value for entered key is: 5
I will execute no matter what
"""

# Question: I can use a simple print statement after the try/except — why use finally?
# ✅ True, but what if the code is inside a function and you're using return statements?
# In that case, normal prints after return won’t run — but the `finally` block will!

# Let's demonstrate this 👇

dic1 = {1: 5, 2: 7, 3: 9}
y = input("Enter key: ")

def finally_check():
    try:
        key1 = int(y)
        # Check if the key exists in the dictionary
        if key1 in dic1:
            print("Value for entered key is:", dic1[key1])
            return "Success"
        else:
            print("Wrong input")
            return "In else"
    except:
        print("Value you have entered is wrong. Make sure it is an integer.")
        return "In except"
    finally:
        print("I will execute no matter what")  # ✅ This will run even if return was used above

# Call the function
result = finally_check()
print("Function returned:", result)

'''
Why is this important?
👉 If you used a normal print after `return`, it wouldn’t run.
👉 `finally` is perfect for cleanup actions like:
   - closing files
   - releasing memory
   - disconnecting database
   - or just logging that something finished
'''
