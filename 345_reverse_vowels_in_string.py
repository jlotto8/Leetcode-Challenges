# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

"""
create an empty string to hold the result
create 2 empty lists, 1 for vowels, 1 for indexes
loop through the string
if letter is not a vowel, add it to the result
if letter is a vowel, add the letter to a list of letters, and the index of the vowel add to a list of indexes

reverse the list of indexes
loop through both lists, insert the letter from letter list into the result, at the index of index list
"""

def reverse_vowels(s):

    result_word = list(s)
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    vowels_list = []
    index_list = []
    for index,letter in enumerate(s):
        if letter in vowels:
            vowels_list.append(letter)
            index_list.append(index)
        else:
            result_word[index]=letter


    reversed_vowels = vowels_list[::-1]
    
    for i,char in zip(index_list,reversed_vowels):
        result_word[i]=char
        result_string= "".join(result_word)
    print(result_string)

reverse_vowels('hello')

     