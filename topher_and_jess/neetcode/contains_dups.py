"""
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

def contains_dup(numbers):

    # seen = set()
    # for num in numbers:
    #     if num not in seen:
    #         seen.add(num)
    #     # else:
    #     return True
    # return False
# print(contains_dup([1, 2, 3]))

    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False
print(contains_dup([1, 2, 3,3]))
