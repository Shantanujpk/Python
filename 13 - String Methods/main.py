# 📘 Python String Methods (Beginner Friendly)

# Note: Strings are immutable - applying a method does NOT change the original string unless reassigned.

# 1. Uppercase
st = '!!!America !!!! America !!'
print(st.upper())  # Output: '!!!AMERICA !!!! AMERICA !!'

# 2. Lowercase
print(st.lower())  # Output: '!!!america !!!! america !!'

# 3. rstrip() - Removes specific characters from the end only
print(st.rstrip("!"))  # Removes trailing '!' only

# 4. replace() - Replace parts of a string
print(st.replace("America", "India"))  # Replace "America" with "India"

# Checking if the original string changed
print(st)  # Original string remains unchanged

# 5. split() - Split string into a list
print(st.split(" "))  # Split by space

# 6. capitalize() - Capitalize the first character
st1 = "master python"
print(st1.capitalize())  # Output: 'Master python'

# 7. center() - Center align the string with a specified width
print(st1.center(50))  # Centers text in 50 spaces

# 8. count() - Count how many times a substring occurs
print(st.count("America"))  # Output: 2

# 9. endswith() - Check if the string ends with a given substring
print(st.endswith("!"))  # True
print(st.endswith("ca", 8, 10))  # True (check between index 8 and 10)

# 10. find() - Find the first occurrence index of a substring
st = "He's name is Dan , He is amazing actor"
print(st.find("is"))  # Output: 10
print(st.find("isasd"))  # Output: -1 (not found)

# 11. index() - Similar to find(), but raises error if not found
# print(st.index("isasd"))  # Uncommenting will raise ValueError

# 12. isalnum() - Check if string is alphanumeric (no spaces)
print(st.isalnum())  # False

# 13. isalpha() - Check if string is alphabetic only (A-Z or a-z)
st = "awesome"
print(st.isalpha())  # True

# 14. islower() - Check if all characters are lowercase
print(st.islower())  # True

# 15. isprintable() - Check if all characters are printable
st = "Hi my name is Dan \n"
print(st.isprintable())  # False because of '\n' (newline)

# 16. isspace() - Check if the string contains only whitespace
print(st.isspace())  # False

# 17. istitle() - Check if each word starts with uppercase
st = "Hi My Name Is Dan"
print(st.istitle())  # True

st = "Hi My name Is Dan"
print(st.istitle())  # False

# 18. startswith() - Check if string starts with a given substring
print(st.startswith("Hi"))  # True

# 19. swapcase() - Swap uppercase to lowercase and vice versa
print(st.swapcase())  # Output: 'hI mY NAME iS dAN'

# 20. title() - Convert string into title case (each word capitalized)
print(st.title())  # Output: 'Hi My Name Is Dan'
