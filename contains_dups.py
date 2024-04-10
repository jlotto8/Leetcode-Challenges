"""
217. Contains Duplicate      Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:   1 <= nums.length <= 105    -109 <= nums[i] <= 109

[5,6,7,8]   4
0  1 2 3 
"""

# def is_duplicate(nums):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# print(is_duplicate([]))

# def is_dup(nums):
#     i = 0
#     count = 0
#     while nums[i] < len(nums):
#         i == nums[i]
#         i += 1
#         if nums[i] == nums[i+1]:
#             print(True)
#             break
#     return False
# print(is_dup([0,1,5,2,3]))


# def dups(nums):
#     i = 0
#     while len(nums) >=1:
#         if nums[i] == nums[i+1]:
#             return True
#         i += 1
#         if i == len(nums)-1:
#             break
#     return False
# print(dups([0,1,2,2]))

def containsDuplicate(nums):
    # TODO: Write your code here
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]== nums[j]:
                return True
    return False
print(containsDuplicate([0,1,2,3,3]))