"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

Recommended Time & Space Complexity
You should aim for a solution with O(m) time for each encode() and decode() call and O(m+n) space, where m is the sum of lengths of all the strings and n is the number of strings.

Hint 1
A naive solution would be to use a non-ascii character as a delimiter. Can you think of a better way?

Hint 2
Try to encode and decode the strings using a smart approach based on the lengths of each string. How can you differentiate between the lengths and any numbers that might be present in the strings?

Hint 3
We can use an encoding approach where we start with a number representing the length of the string, followed by a separator character (let's use # for simplicity), and then the string itself. To decode, we read the number until we reach a #, then use that number to read the specified number of characters as the string.
"""

def encode(strs):

    result = ''
    for s in strs:
        result += str(len(s)) + '*' + s
    return result

print(encode((["neet","code","love","you"])))

"""
decode
I: result one string
O: list returned to original 
C: any utf-8 char
E: consider numbers, other chars etc
4*neet4*code4*love3*you

create variable to store the result
use two pointers/variables to keep track of beginning and end of the word
initialize i to 0 
loop through the encoded string
    find the position of '*': use .index index_of_* = 
    word_length = s[i:j]
    find the length of the word following the '*' index through the length of first pointer :second pointer
    convert to an integer
    change i to the index of_* plus 1 - start of the word is after * 
    index now equal the index of_* plus word_length, plus whatever index is currently iterating
    add the word to the result
"""

def decode(string):

    list_result = list()
    i = 0
    # idx_of_star = 0

    while i < len(string):
        idx_of_star = (string.index('*',i))

        word_length = int(string[i:idx_of_star]) # the number that is the len of the following word
       
        i = idx_of_star + 1
        
        idx_of_star = i + word_length
        list_result.append(string[i:idx_of_star])
        i = idx_of_star
    return list_result

print(decode('4*neet4*code4*love3*you'))
 def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
