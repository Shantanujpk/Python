# Let's learn about Dictionaries in Python using simple examples.

# A dictionary stores information in a pair format like:
# Key -> Value
# Think of it like a notebook where you write someone's name (key) and their phone number (value).

# Basic Syntax of a Dictionary in Python

dictionary_name = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Here's a simple dictionary:
person = {
    "Name": "Dan",
    "Address": "New York",
    "Country": "USA",
    "Age": 25
}

# 1. Show everything inside the dictionary
print(person)  # prints all info

# 2. Check what type of data this is
print(type(person))  # it says <class 'dict'> meaning it's a dictionary

# 3. How to get a specific info? Let's get Dan's name
print(person['Name'])  # This will give: Dan

# 4. Another way to get info safely (won't crash if key is missing)
print(person.get('Age'))  # This will give: 25

# Difference: 
# person['Height'] -> gives error if 'Height' is not found
# person.get('Height') -> just gives None (no crash)

# 5. Get all the keys (like Name, Address, Country, Age)
print(person.keys())

# 6. Print each value using the key
for key in person.keys():
    print(person[key])  # prints each value one by one

# 7. Print each value nicely using f-string (formatting)
for key in person.keys():
    print(f"The value for {key} is {person[key]}")

# 8. Get all the values only
print(person.values())

# 9. See both keys and values together
print(person.items())  # shows pairs like ('Name', 'Dan')

# 10. Loop through both key and value
for key, value in person.items():
    print(f"The value for {key} is {value}")
