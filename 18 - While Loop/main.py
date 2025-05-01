# 📘 While Loop in Python

# ➔ While loop is used to run a block of code **again and again** as long as a condition is True.
# ➔ It is similar to a for loop, but usually used when **you don't know in advance** how many times to loop.

# Syntax:
# while (condition):
#     do something

# ------------------------------------------------------------------------------

# 🖥️ Example 1: Simple While Loop to Count Up

i = 1  # Start value

while (i < 5):  # Condition: Loop will continue as long as i is less than 5
    print(i)
    i = i + 1  # Update step: Increase i by 1 every time

# Output:
# 1
# 2
# 3
# 4

# ------------------------------------------------------------------------------
 
# 🖥️ Example 2: While Loop to Count Down

i = 5  # Start value

while (i > 0):  # Condition: Loop while i is greater than 0
    print(i)
    i = i - 1  # Update step: Decrease i by 1 every time

# Output:
# 5
# 4
# 3
# 2
# 1

# ------------------------------------------------------------------------------
 
# 🖥️ Example 3: While Loop with ELSE Block

i = 1  # Start value

while (i < 5):  # Condition
    print(i)
    i = i + 1
else:
    print("Outside While")  # Once while condition becomes False, else block runs

# Output:
# 1
# 2
# 3
# 4
# Outside While

# Do While Loop : 
# How to emulate do while Loop in python? because in pyhon we dont use do while loop 

# Emulating do-while loop in Python

while True:
    number = int(input("Enter a number greater than 10: "))
    
    if number > 10:
        print("Good job! You entered:", number)
    else:
        print("Try again!")

    # Ask user if they want to continue
    again = input("Do you want to continue? (yes/no): ")

    if again.lower() != "yes":
        print("Exiting the loop. Goodbye!")
        break


# ------------------------------------------------------------------------------

# ✅ Important Notes for Beginners:

# ➔ Both for and while loops are used for repeating actions.
# ➔ Syntax difference: 
#    - 'for' loop is used when you know exactly how many times to repeat.
#    - 'while' loop is better when you **don't know how many times** but you have a condition to check.
#
# ➔ Very important: You must change the variable inside while loop (increment or decrement),
#    otherwise it can create an **infinite loop** (which never stops).

# 🔥 Example of Infinite Loop (Don't run unless you want infinite output):
# while True:
#     print("I will run forever!")

# ➔ The else part in while loop runs **after** the while loop ends naturally (condition becomes False).
