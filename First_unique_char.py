# 387. First Unique Character in a String
# Easy
# 7.3K
# 249
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         frequency = {} # O(1)
#         for char in s: # O(n)
#             if char in frequency: # O(1)
#                 frequency[char] += 1 # O(1)
#             else: # O(1)
#                 frequency[char] = 1 # O(1)
#         for char in s: # O(n)
#             if frequency[char] == 1: # O(1)
#                 return s.index(char) # O(1)
#         return -1 # O(1)
# Time complexity is O(n) + O(n)
    
# Create empty dictioionary
# Loop through string
# Note each letter occurence
# Loop again
# Checking in the dictionary created above if the occurence of the letter is 1
# Return that index
# If the unique letter with occurance 1,  return -1
# Jessica Lotto