"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
   # for i  in range(len(s)):
    #     for j in range(len(t)):
    #         if s[i]  != t[j]:
    #             return False
    #         else:
    #             continue
    # return True

# def is_anagram(s,t):
#     i = 0
#     seen = set()
#     while len(seen) < len(s):
#         # if s[i] in t:
#         seen = seen.add(s[i])
#         i +=1
#         return True
#     if t[i] not in seen:
#         return False
# print(is_anagram("tar", "rat"))

        # if len(s) != len(t):
        #     return False
        # i = 0
        # seen = set()
        # while len(seen) < len(s):
        #     # if s[i] in t:
        #     seen.add(s[i])
        #     if t[i] not in seen:
        #         return False
        #     i += 1
        # return True

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         i = 0
#         while i < len(s):
#             if s[i] != t[i]:
#                 return False
#             i += 1
#         return True

# s = 'aa' t = 'a' output should be false 

# s = "aacc"  t = "ccac" output should be false
"""
add each letter to a dict and counts of each letter
create a dict for each word

check if the dictionaries are the same
"""

def isAnagram(s: str, t: str) -> bool:
    # if len(s) != len(t):
    #     return False
    # else:
    #     word_one_set = set(s)
    #     word_two_set = set(t)
    # return word_one_set == word_two_set

# working solution to account for these edge cases! # s = 'aa' t = 'a' output should be false s = "aacc"  t = "ccac" output should be false
    word_one_dict = dict()
    word_two_dict = dict()

    if len(s) != len(t):
        return False
    for letter in s:
        word_one_dict[letter] = word_one_dict.get(letter,0) +1
    for letter_two in t:
        word_two_dict[letter_two] = word_two_dict.get(letter_two,0) +1

    if word_one_dict == word_two_dict:
        return True
print(isAnagram(s = "aa", t = "a"))
        
