import re

# -------------------------------------------------------
# 🧠 What is a Regular Expression (Regex)?
# -------------------------------------------------------
# Regex is a tool to match, search, and manipulate strings using patterns.

# -------------------------------------------------------
# ✅ Common Regex Functions
# -------------------------------------------------------

# re.match(): Match only from the beginning of a string
print("\n🔍 Using re.match():")
result = re.match(r'Hello', 'Hello world')
print(result.group() if result else "No match")

# re.search(): Match anywhere in the string
print("\n🔍 Using re.search():")
result = re.search(r'world', 'Hello world')
print(result.group() if result else "No match")

# re.findall(): Find all occurrences of a pattern
print("\n🔍 Using re.findall():")
results = re.findall(r'\d+', 'My numbers are 12 and 45')
print(results)  # ['12', '45']

# re.sub(): Replace parts of a string
print("\n🔍 Using re.sub():")
modified = re.sub(r'\s', '-', 'Replace all spaces with dashes')
print(modified)

# -------------------------------------------------------
# 🔣 Meta Characters in Regex
# -------------------------------------------------------
# .   => Any character except newline
# ^   => Start of string
# $   => End of string
# *   => 0 or more repetitions
# +   => 1 or more repetitions
# ?   => 0 or 1 repetition
# {n} => Exactly n repetitions
# {n,}=> At least n repetitions
# {n,m}=> Between n and m repetitions
# []  => Set of characters
# |   => OR
# ()  => Grouping

sample_text = "abc 123 xyz 456"

print("\n🔣 Meta Characters Examples:")

# . (dot) - match any one character
print("Match any character using . :", re.findall(r'a.c', sample_text))

# ^ and $ - anchors
print("Starts with 'abc':", re.match(r'^abc', sample_text))
print("Ends with '456':", re.search(r'456$', sample_text))

# * - 0 or more
# + - 1 or more
print("Digits (1+):", re.findall(r'\d+', sample_text))  # ['123', '456']

# ? - 0 or 1
print("Optional x:", re.findall(r'x?', sample_text))

# {n}, {n,}, {n,m}
print("Exactly 3 digits:", re.findall(r'\d{3}', sample_text))

# [] - Match any one character from the set
print("Match vowels:", re.findall(r'[aeiou]', sample_text))

# | - OR
print("Match 'abc' or 'xyz':", re.findall(r'abc|xyz', sample_text))

# () - Grouping
grouped = re.search(r'(\d+)\s(\w+)', sample_text)
if grouped:
    print("Grouped match (digits + word):", grouped.groups())

# -------------------------------------------------------
# ✅ Raw Strings - Always use r'' for regex patterns
# -------------------------------------------------------

# -------------------------------------------------------
# ✅ Special Sequences Summary
# -------------------------------------------------------

summary = {
    r"\d": "Digit (0-9)",
    r"\D": "Non-digit",
    r"\w": "Word character (a-z, A-Z, 0-9, _)",
    r"\W": "Non-word character",
    r"\s": "Whitespace",
    r"\S": "Non-whitespace",
    r".": "Any character except newline",
    r"^": "Start of string",
    r"$": "End of string"
}

print("\n📘 Regex Special Sequences Summary:")
for pattern, desc in summary.items():
    print(f"{pattern}: {desc}")

print("\n✅ Done! Regular Expressions in Python fully explained.")
