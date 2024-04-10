# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

"""
go through each number in the list of numbers
check the first number in the list to the next number in the list, 
if they are different, keep check the first number against every other number
if they are the same
stop
return True
if at the end of the list, none of the numbers are the same, retturn False
"""

def has_duplicates(nums):
   for i in range(len(nums)):
        for j in range(i +1,len(nums)):
            if nums[i] == nums[j]:
                return True
   return False

print(has_duplicates([1,2,3,4]))


# def has_dups(nums):

#     seen = set()

#     for num in nums:
#         if num in seen:
#             return True
#         if num not in seen:
#             seen.add(num)
#     return False
    
# print(has_dups([1,2,3,4,5,5]))