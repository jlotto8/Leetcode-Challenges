# Pseudocoode
# I- s, a string representing roman numerals
# O- integer- translated from s
# consider creating a dict
# create a variable for the integer integer_converted = 0 
# loop through s for numeral in s: for i in range(len(s)):
        # loop through s again for j in range(len(s))
        # element at index 0 in the first loop should be added to the element a index j + 1 (so the element does not add to itself) integer_converted = i[0] + (j[0]+1)
        #elif i == I and j == V or X:
                # integer_converted = j - i
# return integer_converted

# self.integer_converted = 0
# for i in range(len(s)):
#     for j in range(len(s)):
#         integer_converted = i[0]+ j[0] +1
#     elif i[0] == I and j[0]+1 == V or  j[0] + 1 == X:
#         integer_converted = j - i
# return integer_converted
"""
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
        """
'LVIII'
def romanToInt(s):
        roman = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
        }
        total = 0
        for i in range(len(s)-1): # # Loop through the string up to the second-to-last character as not to go out of range
                if roman[s[i]] < roman[s[i+1]]: # To handle the cases where subtraction is involved, check if the current numeral is smaller than the next numeral. If it is, subtract the current numeral's value from the total.
                         total -= roman[s[i]]
                else:
                         total += roman[s[i]]
        total += roman[[s]-1]  # Add the value of the last numeral to the total.
        return total
print(romanToInt('LVIII'))
        # for i in range(len(s) - 1):
        #         if s[i] not in roman or s[i + 1] not in roman:
        #                 return "Invalid Roman numeral"

        #         if roman[s[i]] < roman[s[i + 1]]:
        #                 total -= roman[s[i]]
        #         else:
        #                 total += roman[s[i]]

        # if s[-1] not in roman:
        #         return "Invalid Roman numeral"
    
        # total += roman[s[-1]]  # Add the value of the last numeral

        # return total

# print(romanToInt('LVIII'))

    