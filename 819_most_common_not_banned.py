"""
819. Most Common Word

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"
 
Constraints:
1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.

Idea 1:

create a dict to store each word, and count
split the string to a list
iterate through the list with a for loop
    if the word is not the banned word
        add it to the dict

iterate thru the dict
find the word with the highest count
"""

# def mostCommonWord(self, paragraph: str, banned: List[str]) -> str: # why is list yellow?
import re

def most_common_word(para,banned):

    wrds = dict()
    # pattern = re.compile(r'\W+')
    # pattern = re.compile(r'[,\.!?]')
    # pattern = re.compile(r'[,\.!?]')
    # para = pattern.split(para)
    # para = para.split()

    # for word in para:
    #     word = word.lower()
    #     word.isalpha()

    # for char in para:
    #     if char.isalpha() or char == "":
    #         continue
    #     else:
    #         para = para.replace(char," ")
    #     print(para)

    for i in "!?',;.":
        para = para.replace(i," ")

    para = para.lower().split()

    for word in para:
        word = word.lower()
        if word not in banned:
            wrds[word] = wrds.get(word,0) +1

    max_wrd = float('-inf')
    common_word = ""

    for word, count in wrds.items():
        if count > max_wrd:
            max_wrd = count
            common_word = word
            
    return common_word
print(most_common_word("..Bob hit a ball, the hit BALL flew far after it's was hit.", ['hit']))
# add something to ignore '.'
# punctuation inside words ex it's ex-friend
# try list comp to remove specific chars, split on blank space
"""
problems
 - strip is not removing punctuation; causing inaccurate dict entries

look up split in docs
trim - maybe remove punctuation, replace
regular expression
re.split - anything that is not a wrd
"""