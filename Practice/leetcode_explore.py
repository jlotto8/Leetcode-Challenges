# def largest_num(nums):

#     max_num = float('-inf')

#     for n in nums:
#         if n > max_num:
#             max_num = n
#     return max_num

# print(largest_num(nums=[7,5,3,56,7,3,9,77]))

"""
Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".
"""

# def is_palindrome(s):

#     left = 0
#     right = len(s)-1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left +=1
#         right -=1
#     return True
# print(is_palindrome('racecar'))

"""
Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""

# def is_pair(nums, target):

#     left = 0 
#     right = len(nums)-1

#     while left < right: 

#         # curr is the current sum
#         curr = nums[left] + nums[right]
#         if curr == target:
#             return True
#         if curr > target:
#             right -= 1
#         else:
#             left += 1
#     return False
# print(is_pair([1,2,6,8,9,14,15],13))

"""
Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
"""

