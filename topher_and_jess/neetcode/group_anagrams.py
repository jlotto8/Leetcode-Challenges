"""
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

{'act': []}
act, opst, opst, act, opst, aht

create an empty dictionary to store the sorted word as the key, and any other matching the key will be added as the value in a list
loop through list of strings
    sort the string
    check if it is in the dict
        if it is, add the word to the list
        if not, add to the dictionary
"""

def group_anagrams(strings):

    anagram_groups = dict()

    for word in strings:
        sorted_word = ''.join(sorted(word))
        # print(sorted_word)

        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    return list(anagram_groups.values())
print(group_anagrams(["act","pots","tops","cat","stop","hat"]))