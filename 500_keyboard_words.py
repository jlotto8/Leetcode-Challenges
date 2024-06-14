"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:
1 <= words.length <= 20; 1 <= words[i].length <= 100words;[i] consists of English letters (both lower and uppercase)

Plan 1

create an empty list to hold the result words
create a set of each row of letters in the keyboard row_one = set(qwertyuiop) row_2 = set(asdfghjkl) row_3 = set(zxcvbnm)
loop through the list of words
    create a flag called invalid_leter and set to False
    loop through each letter in the word
        if the letter in the word is not in one of the set of keyboard letters:
            flag becomes true
            stop looping
    if flag is false and if all the letters in the word are in one set
        add the word to the results list

Problems:

1. how do I check if the letters are in 3 different sets? Long ineffecient code? 
create a function 29-35 I: list of words, set of keyboard letters output- boolean/output of flag
2. this is O(n**2); would it improve if I loop through the words and add them to a set instead of a list? what if I cast the given list of words to a set? would still be able to check each letter in each word?

solve first with one keyboard row, then create a function to check with each keyboard row 
case sensitivity

can word x be made with row y
call the function 3 times for 3 sets of letters

"""
def get_keyboard_words(words,keyboard_row):

    result_words = []

    for word in words:
        word = word.lower()

        invalid_letter = False

        for letter in word:
            if letter not in keyboard_row:
                invalid_letter = True
                break

        if invalid_letter == False:
            result_words.append(word)

    return result_words

print(get_keyboard_words(["Hello","Alaska","Dad","Peace"],keyboard_row=set("a,s,d,f,g,h,j,k,l")))

# function to take one word, one keyboard set; return true or false if the word is in the set

"""
Leetcode solutions:

l1="qwertyuiop"
l2="asdfghjkl"
l3="zxcvbnm"
res=[]
for word in words:
    w=word.lower()
    if len(set(l1+w))==len(l1) or len(set(l2+w))==len(l2) or len(set(l3+w))==len(l3) :
        res.append(word)
return res

set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}
        
        res = []
        for i in words:
            wordset = set(i.lower())
            if (wordset&set1 == wordset) or (wordset&set2 == wordset) or (wordset&set3 == wordset):
                res.append(i)
        return res
"""
