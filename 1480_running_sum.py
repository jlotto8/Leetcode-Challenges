"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 
Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

import typing
from typing import List

# def runningSum(nums):

nums = [1,2,3,4]
# right = 0
# result_lst = []
# for left in range(len(nums)):
#     total = 0
#     result_lst = [nums[left]]
#     total += nums[left] + nums[right]
#     print(f'left = {left}, element = {nums[left]}, right = {right}, element = {nums[right]},total = {total}, result = {result_lst}')
#     result_lst.append(total)
#     right += 1
# return result_lst
# print(runningSum([[1,2,3,4]]))

# nums = [1,2,3,4]
# right = 1
# left = 0
# sum_1 = 0
# results = []

# while left < len(nums):
#     sum_1 += nums[left]
#     print(f'left = {left}, element = {nums[left]}, right = {right}, element = {nums[right]},total = {sum_1}, result = {results}')
#     results.append(sum_1)
#     left += 1
#     right += 1

# print(results)
# input [1,2,3,4]
# Output: [1,3,6,10]

nums = [1,2,3,4]
results = []
total = 0

for i in range(len(nums)):
        total += nums[i] 
        results.append(total)
print(results)

