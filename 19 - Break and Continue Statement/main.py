# Example of break statement

# Loop to print table of 5, but stop when result is 50
for i in range(10):  # i goes from 0 to 9
    if i == 9:  # When i is 9, 5 * (i+1) = 50
        break  # Exit the loop
    print("Table of 5:", 5 * (i + 1))
print("Out of Loop")


# Example of continue statement

# Loop to print table of 5, but skip when result is 55
for i in range(12):  # i goes from 0 to 11
    if i == 10:  # When i is 10, 5 * (i+1) = 55
        continue  # Skip this iteration
    print("Table of 5:", 5 * (i + 1))
print("Out of Loop")


# Break with list example

print("List break example")
numbers = [2, 4, 6, 8, 10, 11, 12]

for num in numbers:
    if num % 2 != 0:  # If number is odd
        break  # Exit loop
    print(num)


# Continue with list example

print("List continue example")
numbers = [2, 4, 6, 8, 10, 11, 12]

for num in numbers:
    if num % 2 != 0:  # If number is odd
        continue  # Skip this number
    print(num)
