# 884. Uncommon Words from Two Sentences

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]

# Example 2:
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
 

# Constraints:
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.

word_counts = dict()
word_2_counts = dict()

results = []

s1 = 'this apple is sweet'
s2 = 'this apple is sour'

for word in s1.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word_2 in s2.split():
    if word_2 in word_2_counts:
        word_2_counts[word] += 1
    else: 
        word_2_counts[word_2] = 1

for value in word_counts.values():
    if value >1:
        results.append(value)

for value_2 in word_2_counts.values():
    if value_2 >1:
        results.append(value)
print(results)
# results = []

# word = set()
# word_2 = set()

# for word in 
