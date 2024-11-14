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
if all the letters in the first word were in the char string, add the word to a results list

then loop through the results list and create a variable to hold the value of adding the length of each str together
"""

def good_strings(word_list, char_string):

    char_count_dict = dict()
    for char in char_string:
        char_count_dict[char] = char_count_dict.get(char,0)+1 

    good_string_results = []

    for word in word_list:
        word_dict = dict()

        for letter in word:
            word_dict[letter] = word_dict.get(letter,0)+1
            # if the same amount of letters in word_dict are in char_count_dict, add the word to a results list

# this could be a lamda that checks if something is true for an item 
# all() if all()word_dict.items   after a '.' is a method 
        good_word = True
        for let,count in word_dict.items():
            if count > char_count_dict.get(let,0):
            # if char_count_dict.get(let,0) < count:
                good_word = False
                break                
        if good_word:
            good_string_results.append(word)
# can use list comp to get good words

    char_len = 0
    for word in good_string_results:
        # char_len = char_len + len(word)
        char_len += len(word) # why am i getting the error that it is an undefined variable if I try += here?
    return char_len

print(good_strings(["cat","bt","hat","tree"],'atach'))