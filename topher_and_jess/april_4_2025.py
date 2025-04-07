"""
Given a string s, return the index of the first non-repeating character in it. If there is no such character, return -1.

1 <= len(s) <= 10^5

s consists of only lowercase English letters.

🔁 Example 1:
Input: s = "leetcode"
Output: 0
Explanation: 'l' is the first character that appears only once.

🔁 Example 2:
Input: s = "loveleetcode"
Output: 2
Explanation: 'v' is the first character that appears only once.

🔁 Example 3:
Input: s = "aabb"
Output: -1
Explanation: Every character repeats.


I: s, a string
O: index of first non-repeating character, an integer
C: len(s) <= 10 ^5
E: empty string, string of all the same letters

plan 
create a variable to store the result of the index
create a dict to store each letter and their counts
loop through the string s
    if the letter is not in the dict, add it
    else add to the count
get the first key with a count of 1 that was added to the dict
get the index of that key
return the index
if none, return -1
"""

def find_non_rep_char(s):

    dict_of_chars = dict()

    for char in s:
        if char not in dict_of_chars:
            dict_of_chars[char] = 1
        else:
            dict_of_chars[char] += 1

        if dict_of_chars[char] == 1:
            return dict_of_chars.keys()
        else:
            return -1
print(find_non_rep_char('leetcode'))