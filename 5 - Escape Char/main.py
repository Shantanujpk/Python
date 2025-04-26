# ----------------------------------------------
# Python Basics: Escape Sequences, Comments, and Print Parameters
# ----------------------------------------------

# Escape Sequences:
# Escape sequences are special characters used inside strings to format the output.
# For example, "\n" is used to insert a new line.
# "\" inside strings is used to insert double quotes.

# Printing with escape sequences:
print("I am a master's student\nand also an experienced TIBCO Developer")

# Printing with both \n (new line) and \" (double quotes inside text)
print("I am a master's \"student\"\nand also an experienced \"TIBCO\" Developer")

# ----------------------------------------------
# Comments in Python:
# Comments are notes in the code that are ignored during execution.
# They are used to explain what the code is doing.
# Single-line comments start with a "#" symbol.

# Example of a comment:
# This is a single-line comment explaining the code.

# Multi-line comments can be written using triple quotes ''' ''' or """ """.
'''
This is a multiline comment.
Useful for larger explanations.
'''

# ----------------------------------------------
# Tips:
# - To comment multiple lines quickly, you can use:
#   Ctrl + / (Windows/Linux)
#   Command + / (Mac)
#   This shortcut toggles comments on selected lines.

# ----------------------------------------------
# Advanced Print Function:
# By default, Python separates printed values with a space.
# You can customize separators and endings using 'sep' and 'end' parameters.

# Example using 'sep' and 'end' parameters:
print("Hey", 6, 9, sep="~", end="009\n")  # sep="~" separates values, end="009\n" adds custom end

# This will continue on the next line after appending 009.
print("New Line")

# ----------------------------------------------
# Summary:
# - Escape sequences like \n and \" format strings.
# - Use '#' for single-line comments.
# - Use triple quotes for multi-line comments.
# - Customize 'print()' output with 'sep' and 'end' parameters.
# ----------------------------------------------
