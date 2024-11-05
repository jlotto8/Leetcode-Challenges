"""
1160. Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 
Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.

I: list of strings and a string of characters in lowercase
O: integer of the sum of each length of good strings
C: lowercase input
E: each char in the input str can only be used once

create a list to hold the 'good' strings
look at the first word in the list, check if the first letter in the first word is in the char str
if it is, remove that letter from the char str since letters can only be used once, then check the next letter in the first word, and continue the same steps until the end of the word
if al the letters in the first word were in the char string, add the word to a results list

"""