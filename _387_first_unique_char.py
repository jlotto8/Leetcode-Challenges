# 387. First Unique Character in a String

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

"""
start with the first letter of the string, until the end of the string
compare it to the second letter of the string
if the letters are the same, move each comparison to the right, keep checking
if the letters are not the same, return the left most comparision pointer index

loop through each character in the string
check if the characters at those indices are the same
if they are the same, increment both variables by 1
if they are not the same, return the first index - leftmost index variable

"""

def unique_index(s):
    # for i in range(len(s)):
    #     for j in range(i+1,len(s)):
    #         if s[i] == s[j]:
    #             i += 1
    #             j += 1
    #     return i
    # return -1



    for i in range(len(s)):
        repeated = False
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                repeated = True
                break
        if not repeated:
            return i
    return -1
print(unique_index('aabb'))
