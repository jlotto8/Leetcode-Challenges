"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
 
Constraints:
0 <= num <= 231 - 1

naive solution
continue to sum the input numbers until there is one digit left

num = num.to_s.chars.map{|x| x.to_i}.sum 

# consider list comprehension; using sum function 

# solve this in js
- look up each translation

"""

def addDigits(num):
  
    while num >= 10:  # until the number is one digit
        sum_digits = 0  # initialize the sum 
        num_str = str(num)  # convert the number to a string to iterate over easily
        
        for digit in num_str: # loop over each digit one at a time
            sum_digits += int(digit)  # convert char to integer and add to sum
        
        num = sum_digits  # Update num with the sum of its digits

    return num  

print(addDigits(38))  

# what is the O(n)? O log n  log base 10 of n

"""
If number is divisible by 9
then digital root(ans) is 9
else the digital root is remainder

(num - 1) % 9 + 1

# significance of 0 
# % 9 possible 0-8 ; need 1-9

"""
def addDigits(num):
    if num == 0:
        return 0
    return (num - 1) % 9 + 1

# neg numbers % 9 in python?
# 0(1)

# recursion?
# base case 1 digit
# add digits 
# return last thing
# tail recursion can just be a while loop
