"""
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100å
words[i] consists of lowercase English letters.

look at each letter in the first word, check if that letter is in the other words
if it is, add the letter to a list
if it is not, go on to the next letter in the first word until there are no more letters

or

add each letter of each word to it's own dictionary as the key, count the letters in the word as the value
check if the values of each dictionary are 
if they are the same, add them to a list


I: list of words/strings
O: list of characters 
E: empty list of words; 1 word, 1 letter
C: above

create a results list
loop through the list of  words
    loop thru each letter
        if letter is in each word
            add the letter to a list
return resuults llist of letters
O(n**2)

Create a results list
loop thru words
    create a dictionary for each word, add each letter and a count of each letter

    compare the values of each dict, if they are the same- ** minimum **
        add the values to a results list
return the list


Create a dict of the count of each char
Create a list to store the dictionaries
Loop thru each word
    add counts of chars and store in the list

to compare the dicts

loop through the list of dictionaries
    if there are common chars, get the minimum value of the key
    add the value to a results list
return results list

"""

from collections import Counter

words = ["bella","label","roller"]

# count_all_dicts = []

# for word in words:
#     count_dict = Counter(word)
#     count_all_dicts.append(count_dict)
# (

def get_common_chars(words):

    # common_char_count = Counter(words[0])

    # for word in words[1:]:
    #     word_counter = Counter(word)
    #     for char in common_char_count:
    #         common_char_count[char] = min(common_char_count[char], word_counter[char])

    # results = []

    # for char, frequency in common_char_count.items():
    #     results.append([char]) # need the char the # of times it appears






#     common_char_list = []

#     for word in words:
#         for char in word:
#             if char in words:
#                 print(char)
#                 common_char_list.append(char)
#     return common_char_list

# print(get_common_chars(["bella","label","roller"])