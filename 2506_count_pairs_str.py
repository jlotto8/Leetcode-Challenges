"""

2506. Count Pairs Of Similar Strings

You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

Example 1:
Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 

Example 2:
Input: words = ["aabb","ab","ba"]
Output: 3
Explanation: There are 3 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
- i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.

Example 3:
Input: words = ["nba","cba","dba"]
Output: 0
Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.
 
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consist of only lowercase English letters.


dictionary
subsets 

"""

def similar_pairs(words):
    # dict to count each unique set of chars/str
    char_set_count = {}
    
    for word in words:
        # convert str to a set and make it a frozenset b/c sets cannot be keys (immutable)
        char_set = frozenset(word)
        
        # Add or update the count for this frozenset in the dictionary
        if char_set in char_set_count:
            char_set_count[char_set] += 1
        else:
            char_set_count[char_set] = 1
    
    # Calculate the number of pairs
    pairs = 0
    for count in char_set_count.values():
        if count > 1:
            # Calculate the number of pairs from count occurrences
            pairs += (count * (count - 1)) // 2
    
    return pairs

# Test cases
print(similar_pairs(["aba", "aabb", "abcd", "bac", "aabc"]))  # Output: 2
print(similar_pairs(["aabb", "ab", "ba"]))                   # Output: 3
print(similar_pairs(["nba", "cba", "dba"]))                  # Output: 0
 