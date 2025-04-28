"""
# Expected Output
# [1, 4, 9, 16]

Task: Take a list of numbers and return a list of their squares.
for loop then list comp
"""

squares = []
nums = [1, 2, 3, 4]

# for n in nums:
#     sqr = n ** 2
#     squares.append(sqr)
# print(squares)

square = [n ** 2 for n in nums]

# print(square)

"""
2. Filtering Elements
Task: Return only the even numbers from a list.

# Expected Output
# [2, 4, 6]
"""
nums = [1, 2, 3, 4, 5, 6]

evens = [n for n in nums if n % 2 == 0]
# print(evens)

"""
3. Strings to Uppercase
Task: Convert a list of strings to uppercase.

# Expected Output
# ['HELLO', 'WORLD', 'PYTHON']
"""
words = ['hello', 'world', 'python']

uppers = [word.upper() for word in words]
# print(uppers)

"""
4. Add Condition: Strings with More Than 4 Letters
Task: From a list of strings, return only the ones longer than 4 characters.

# Expected Output
# ['hello', 'goodbye']
"""
words = ['hi', 'hello', 'yes', 'goodbye']

long = [word for word in words if len(word) > 4]
# print(long)

"""
5. Pairing Indexes and Values
Task: Create a list of strings like "Index 0: hello" from a list of words.

# Expected Output
# ['Index 0: apple', 'Index 1: banana', 'Index 2: cherry']
"""
words = ['apple', 'banana', 'cherry']

strings = [f'Index {word.index(word)}: {word}' for word in words]
print(strings)