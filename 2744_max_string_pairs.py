"""
You are given a 0-indexed array words consisting of distinct strings.
The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.
Return the maximum number of pairs that can be formed from the array words.
Note that each string can belong in at most one pair.

Example 1:
Input: words = ["cd","ac","dc","ca","zz"]
Output: 2
Explanation: In this example, we can form 2 pair of strings in the following way:
- We pair the 0th string with the 2nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
- We pair the 1st string with the 3rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
It can be proven that 2 is the maximum number of pairs that can be formed.

Example 2:
Input: words = ["ab","ba","cc"]
Output: 1
Explanation: In this example, we can form 1 pair of strings in the following way:
- We pair the 0th string with the 1st string, as the reversed string of words[1] is "ab" and is equal to words[0].
It can be proven that 1 is the maximum number of pairs that can be formed.

Example 3:
Input: words = ["aa","ab"]
Output: 0
Explanation: In this example, we are unable to form any pair of strings.

Idea 1:

create an accumulator called pairs, initialiize to 0
loop through the list of string = words
    create a list of strings with each string reversed = reversed_words
loop through the list of reversed words
    if the string in words is in the list of reveresed words:
        increment pairs by 1

Idea 2:

Create an accumulator called pairs, initialize to 0
Create a set of reversed strings from the word list
loop through the words list
    if the string is in the set of reversed words
        increment pairs # this will double the result
    
Neither of these will work- all I'm doing by creating a reveresed list is still checking if the original string is there...not if it is there reversed

I need to check if 'ac' is == reversed('ac')

Idea 3:

{'cd':'dc', 'ac':'ca', 'dc':'cd', 'ca':'ac', 'zz':'zz'}

pairs = 0
create a dictionary with key value pairs of the original string, and the string reversed
loop through the dictionary
    loop through it again
        check if a key is equal to a value- any value in the dictionary
            if it is, increment pairs
problems - 'zz' one string with the same letters reversed needs to not be counted as a pair
- ouput is incorrect with this implementation, pairs are counted twice, doubling the output
Fixed these problems and coded a solution, but it is not an efficient solution O(n**2)

"""
# finding best way to reverse a string:

# def maximumNumberOfStringPairs(words):
# str_one = 'ac'
# reversed_string = "".join(reversed(str_one)) 
# print(reversed_string) # why does this print <reversed object at 0x101bcfc10> 

# pairs = []
# for letter in reversed_string:
#     pairs.append(letter)
# print(pairs) # but this prints c,a

        
    # reversed_words_set.add(reversed_word)
        # print(reversed_word)
words = ["cd","ac","dc","ca","zz"]

# reversed_words_set = set()
# for word in words:
#     for i in range(len(word)):
#         reversed_word = word[i::-1]
#     reversed_words_set.add(reversed_word)
# # print(reversed_words_set)

# for i in range(len(words)):
#     words[i]

# finally figured out correct syntax to reverse the string, kill me words[i][::-1]


# words = ["cd","ac","dc","ca","zz"]
# str_and_rev_str_dict = dict()
# for i in range(len(words)):
#     str_and_rev_str_dict[words[i]] = str_and_rev_str_dict.get(words[i],words[i][::-1])
# # print(str_and_rev_str_dict)

# pairs = 0
# for key,value in str_and_rev_str_dict.items():
#     if key == value:
#     # print(key)
#         pairs += 1
# # print(pairs)


# #     if str_and_rev_str_dict.keys() == str_and_rev_str_dict.values():
# #         pairs +=1
# # print(pairs)

# words = ['ab','ba']
# words_dict = {'ab':'ba','ba':'ab'}
# this doubles the output

# reversed_words = []
# for i in range(len(words)):
#     reversed_word = words[::-1]
#     reversed_words.append(reversed_word)
# words = ['ab','ba','zz','rl']
# reversed_words = ['ba', 'ab', 'zz', 'lr']
# for word in words:
#     reversed_word = word[::-1]
#     reversed_words.append(reversed_word)
# print(reversed_words)

# pairs = 0
# set_of_str = set()
# for i in range(len(words)):
#     rev_word = words[i][::-1]
#     if rev_word == words[i]: # to account for 'zz'
#         set_of_str.add(words[i])
#     if rev_word in words:
#         pairs += 1
#         if rev_word in set_of_str: # 'remove zz'
#             pairs -= 1
# print(int(pairs/2))
# O(n) * m (m is len of each word)

# pairs = 0
# set_duplicate_letters = set()

# for i in range(len(words)):
#     rev_word = words[i][::-1]
#     # (print(rev_word,words[i]))
#     if rev_word == words[i]: # to account for 'zz'
#         # words.remove(word[i])
#         set_of_str.add(words[i]) 
#     if rev_word in words:
#         pairs += 1
#         if rev_word in set_duplicate_letters: # 'remove zz'
#             pairs -= 1
# print(int(pairs/2))

# pairs = 0
# set_duplicate_letters = set()
# pairs_of_str_without_dup_letters = []

#This and the solution below do not work because i modify the original list
# for i in range(len(words)):
#     rev_word = words[i][::-1]
#     # (print(rev_word,words[i]))
#     if rev_word == words[i]: # to account for 'zz'
#         # pairs_of_str_without_dup_letters = words.remove(words[i])
#         words.remove(words[i])
#         print(words)
#         # set_duplicate_letters.add(words[i])
#         if rev_word in words:
#             pairs += 1
        # if rev_word in set_duplicate_letters: # 'remove zz'
            # pairs -= 1
# print(int(pairs/2))

# for word in words:
#     rev_word = word[::-1]
#     if rev_word == word:
#         words.remove(word)
#     elif rev_word in words:
#         pairs += 1
# print(int(pairs/2))
# this and the code above get index of range error because I modify the size of words by removing a word from it
# words = ['ab','ba','zz','rl']

# This solves index out of range error by making a copy of the original list

# words_copy = copy(words)
# for i in range(len(words)):
#     rev_word = words[i][::-1]
#     # (print(rev_word,words[i]))
#     if rev_word == words[i]: # to account for 'zz'
#         # pairs_of_str_without_dup_letters = words.remove(words[i])
#         words.remove(words[i])
#         print(words)
#         # set_duplicate_letters.add(words[i])
#         if rev_word in words:
#             pairs += 1
        # if rev_word in set_duplicate_letters: # 'remove zz'
            # pairs -= 1

# pairs = 0
# words_copy = words.copy()  # Create a copy of the original list

# for word in words_copy:
#     rev_word = word[::-1]  
#     if rev_word == word:
#         words.remove(word)
#     elif rev_word in words:
#         pairs += 1
# print(int(pairs / 2))

# O(n **2) this is just styled better than my first try, which added str with duplicate letters to a set, then decremented pairs if the word was in the set 

words = ["cd","ac","dc","ca","zz"]
pairs = 0
reversed_words_set = set()
for i in range(len(words)):
    reversed_words_set.add(words[i][::-1])
    if words[i][::-1] == words[i]:
        reversed_words_set.remove(words[i])
    if words[i] in reversed_words_set:
        pairs += 1
print(int(pairs))

# This should improve the time complexity because instead of checking if the word is in the list again, it's checking if the word is in a set- which is more effecient. Not sure if this is O(n) or O(n * m)

