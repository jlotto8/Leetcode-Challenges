# d = digits[-1]+1
# # l=d+1
# digits[-1] = d
# return  digits
# if len(digits[-1]>1):
#     # digits[0]+=1
#     digits= digits[-1]
"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

When you add the current digit in the digits array and the carry, you get current_sum.
current_sum % 10 gives you the last digit of current_sum.
This last digit is then appended to the result array.
For example, if current_sum is 13, then current_sum % 10 would be 3. If current_sum is 27, then current_sum % 10 would be 7. It ensures that only the last digit is considered and added to the result.

try again with exponents for next week
"""
# digits = [1,2,3]
# def plusone(digits):
#     carry = 1  # Initialize carry to 1, as we are incrementing by one
#     result = []
#     for i in range(len(digits) - 1, -1, -1):
#         current_sum = digits[i] + carry
#         result.append(current_sum % 10)  # Append the remainder to the result
#         carry = current_sum // 10  # Update carry for the next iteration
#     if carry:# if after all digits are looped
#         result.append(carry)
#     return result[::-1]  # Reverse the result to get the correct order

def plusOne(digits):
    num = 0 # Initialize accumulator for the numerical value represented by the input digits
    for i in range(len(digits)):
        num += digits[i] * pow(10,(len(digits)-1-i))  # * pow(10, ...calculates the place value of the digit. It uses the pow function to raise 10 to the power of (len(digits)-1-i). The exponent (len(digits)-1-i) is used because the right-most digit is in the ones place, the next digit to the left is in the tens place, and so on. This exponentially converts each digit to its corresponding place value. 
        # digits[i] * This multiplies the current digit by its place value, giving the numerical value of the digit in the context of its position in the number.
    result = []
    for i in str(num+1):
        result.append(int(i))#convert back to a list and add 1
    return result
print(plusOne([1,2,3]))
"""
Question for mentor:
I don't understand this:
Using % you can extract the right most digit or digits from a number- for example x % 10 yields the right-most digit of x (in base 10), x % 100 yields the last two digits
"""
# use % to solve using exponents

# def plusOne(digits):
#     num_string = '' # initialize an empty str
#     for i in digits: # loop through digits list 
#         num_string += str(i) #add each int in digits to num_string, use str( to convert int to str
#         nums = int(num_string) # convert nums to int 
#         nums+= 1 # so I can perform the addition
#         s =  str(nums) #convert the int result to a string
#     result = [] # initaliize a new list
#     for i in s: # loop through 
#         result.append(int(i))
#     return result
# print(plusOne([1,2,3]))


# def plusOne(digits):
#     n_str = ''
#     i = 0
#     while i < len(digits): #how do I use while True?
#         n_str += str(digits[i])
#         i += 1
#     nums = int(n_str)
#     nums += 1
#     s = str(nums)

#     result = []
#     x = 0
#     while x < len(s):
#         result.append(int(s[x]))
#         x += 1
#     return result
# print(plusOne([1,2,3]))


