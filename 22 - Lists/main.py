# ✅ Creating a list
my_list = ["apple", "banana", "mango", "grape", "orange", 1, 2]

# ✅ Indexing
print(my_list[0])   # 'apple' - first element (index starts from 0)
print(my_list[3])   # 'grape' - fourth element
print(my_list[-1])  # 2 - last element (negative index)
print(my_list[-3])  # 'orange' - third from last

# ✅ Slice Notation
print(my_list[:])       # All elements
print(my_list[1:])      # From index 1 to end
print(my_list[:4])      # From beginning to index 3
print(my_list[1:-2])    # From index 1 to third last (exclusive)
print(my_list[1:7:2])   # From index 1 to 6, jumping 2 steps: ['banana', 'grape', 1]

# Explanation:
# [:6] means start from beginning (default 0) to index 5
# [2:] means start from index 2 to end (default is len(list))

# ✅ Membership Test
print("apple" in my_list)     # True
print(1 in my_list)           # True
print("1" in my_list)         # False - '1' is string, 1 is int

# ✅ List Comprehension (Simple)
squares = [x*x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# ✅ List Comprehension (With Condition)
even_squares = [x*x for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# ✅ Extracting values from another list
words = ["apple", "banana", "mango", "kiwi"]
short_words = [word for word in words if len(word) <= 5]
print(short_words)  # ['apple', 'mango', 'kiwi']
