"""
1342. Number of Steps to Reduce a Number to Zero

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

counter = 0
when num has an operation performed on it, / or -, accumulate the counter


Example 1:
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.

Example 2:
Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.

Example 3:
Input: num = 123
Output: 12
 
Constraints:

0 <= num <= 106
"""

# num = 3
# counter_num = 0
# steps = []
# result = float('inf')

# while result > 0:

#     if num % 2 == 0:
#         result = int(num / 2)
#         num = result
#     # counter_num += 1
#         steps.append(result)
#         # print(f' for division: counter = {steps}, result =  {result}')
#     else:
#         result = num -1
#         num = result
#         # counter_num += 1
#         steps.append(result)
#     # print(f' for subtraction: counter = {steps}, result =  {result}')

# # print(counter_num)
# print(len(steps))

def numberOfSteps(num):

    steps = 0
    result = num

    while result != 0:

        if result % 2 == 0:
            result = result/2
        else: 
            result = result - 1
        steps += 1
    return steps

print(numberOfSteps(14))