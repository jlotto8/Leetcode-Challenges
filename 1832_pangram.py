"""
1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false
 
Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.

I: string lower-case letters
O: booleon true or false
C: lowercase english letters
E: empty string, other chars besides letters

create a dictionary  to store letters and counts of each letter
loop thru the string
    check if letter is in dict, if not add it, if yes, increase the count
check if dict has 26 keys
if  yes, return true
if no return false
"""

def pangram(s):
    
    letter_counts = dict()
    for char in s:
        if char.isalpha():
            char = char.lower()
            if char not in letter_counts:
                letter_counts[char] = letter_counts.get(char,0) +1
    if len(letter_counts) < 26:
        return False
    return True

print(pangram("thequickbrownfoxjumpsoverthelazydoG"))