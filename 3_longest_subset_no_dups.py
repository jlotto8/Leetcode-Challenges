"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104; s consists of English letters, digits, symbols and spaces.
"""
"""
set a variable to current_max = 0
set a variable to current_letters = ""
set a variable to previous letter
set a results variable to an empty string
loop through the string
    check if the letter is different from the previous letter i-1
        if they are different, 
        current longest sub = the string from the previous letter to the letter
        current max length= len(current letters)
    keep checking until the end of the string

sliding window
create an empty set to store each letter
create 2 pointers, left and right
loop through the string
    while the last letter in the string is in the set:
        
        add each letter to the set 
        s = "abcabcbb"
"""

# the execution of each loop is confusing me
def lengthOfLongestSubstring(s: str) -> int:
    letter_set = set()
    l = 0
    longest_substr = 0

    for r in range(len(s)):
        while s[r] in letter_set: 
            letter_set.remove(s[l]) # s[r] is already in the set at this point in the loop?
            l += 1
        letter_set.add(s[r])
        longest_substr = max(longest_substr,r-l +1)
    return longest_substr
print(lengthOfLongestSubstring(s = "abcabcbb"))

# are most sliding window problems solved with code like this - create a range with a for loop to go through the string, then a while loop inside?