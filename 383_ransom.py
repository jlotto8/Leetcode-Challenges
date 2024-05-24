"""
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

ransomNote = {'a': 2}  magazine = {'a': 2,'b': 1}

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

def canConstruct(ransomNote,magazine):
    
    ransom = dict()
    magazine_dict = dict()

    for letter in ransomNote:
        ransom[letter] = ransom.get(letter,0) +1
    
    for letter in magazine:
        magazine_dict[letter] = magazine_dict.get(letter,0) +1
    
    
    ransom_tuples = tuple()

    for key,value in ransom.items():
        ransom_tuples = key,value

    # for letter in ransom_tuples:
    #     if ransom_tuples[2] == magazine_dict.values:
    
    if ransom in magazine_dict:
        if ransom.values in magazine_dict:
            return True
        return False
print(canConstruct(ransomNote = "aa", magazine = "ab"))