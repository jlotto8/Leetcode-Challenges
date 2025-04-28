"""
Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)
O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.

Hint 1
A brute-force solution would be to iterate through the array with index i and compute the product of the array except for that index element. This would be an O(n^2) solution. Can you think of a better way?

Hint 2
Is there a way to avoid the repeated work? Maybe we can store the results of the repeated work in an array.

Hint 3
We can use the prefix and suffix technique. First, we iterate from left to right and store the prefix products for each index in a prefix array, excluding the current index's number. Then, we iterate from right to left and store the suffix products for each index in a suffix array, also excluding the current index's number. Can you figure out the solution from here?

Hint 4
We can use the stored prefix and suffix products to compute the result array by iterating through the array and simply multiplying the prefix and suffix products at each index.

Input: nums = [1,2,4,6]
Output: [48,24,12,8]

create list to store prefixes, initialize with 1 because there is nothing to the left of the first element to muliply by
create list to store postfixes, initialize with h1 because there is notihng to the right of the last element to multiply by
create a list to store results
create variable for length of input len(nums)
loop through nums
    multiply element to the left by 1 initially 
    add result to prefix list 
    multiply next element by the product in prefix
prefix[0] = 1
prefix[1] = nums[0] * 1 = 1
prefix[2] = nums[1] * prefix[1] = 2
prefix[3] = nums[2] * prefix[2] 
[1,1,2,8]

postfix[3] = 1
postfix[2] = postfix[3] * nums[3] = 1 * 6 = 6
postfix[1] = postfix[2] * nums[2] = 
postfix[0] =
"""

def product_except_self(nums):

    length = len(nums)
    prefix = [1]
    postfix = [1]
    output = []