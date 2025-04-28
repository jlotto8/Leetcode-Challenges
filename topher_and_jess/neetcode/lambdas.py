"""
Practice Exercise 1 (EASY)
Try writing a lambda function that:

Takes one number
Returns that number squared

You should:
Save the lambda to a variable called square
Call it with the number 5
Print the result (it should be 25)
"""

square = lambda x: x **2
# print(square(5))

"""
Practice Exercise 2
Write a lambda function that:

Takes two numbers as input
Returns the larger of the two numbers
Hint: You can use the if expression right inside the lambda, like this:

lambda a, b: a if a > b else b
Your steps:
Save it to a variable called maximum

Use it to find the larger of 10 and 7

Print the result (should be 10)
"""
maximum = lambda a, b: a if a > b else b
print(maximum(10, 7))