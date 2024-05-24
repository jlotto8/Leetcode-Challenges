"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

Idea 1:

create a results variable to store the longest repeating window size
create a dict to hold the letters and their counts

create 2 pointers, right and left to create a window- both start at 0
right pointer will start at index 0 and iterate by 1 with a for loop

loop through the string
    add letter and count to the dictionary
    calculate the length of the window - the most frequent letter count - this is how many letters need to be replaced to make them all the same letter  
    check if the number of letters that need to be replaced is less than or equal to k
    if the changes are > k
        increment the left pointer, and decrease the dict count of that letter
    if the changes are not > k:
        update result to the length of the window
        "ABAB"
        "AABABBA"   A:2 B:1 
"""

def longest_char_replacement(string_letters, k):

    result = 0
    letters = dict()
    left = 0

    for right in range(len(string_letters)):
        letters[string_letters[right]] = letters.get(string_letters[right],0) +1
        if (right - left + 1) - max(letters.values()) > k:
            letters[string_letters[left]] -= 1
            left += 1
        result = (right - left +1)
    return result

print(longest_char_replacement("AABABBA",1))

