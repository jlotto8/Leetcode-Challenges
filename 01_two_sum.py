"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 104; -109 <= nums[i] <= 109; -109 <= target <= 109;  Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

Input: nums = [3,2,4], target = 6
Output: [1,2]

if nums[i] + nums[i+1] == target
return i,i+1
"""


# def find_indices(nums, target):
    # nums = sorted(nums)
    # for i in range(len(nums)-1):
    #     if nums[i] + nums[i+1] == target:
    #         print(nums[i], nums[i+1])
    #         return i, i+1
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return i,j
# print(find_indices([3,2,3],6)) 
        
# def twoSum(nums,target):
#     for i in range(len(nums)):
#         x = target - nums[i]
#         if x in nums:
#             y = i
#     return nums.index(x),y
# print(twoSum([3,2,3],6))
"""
create a dictionary to store the numbers in the list nums, and the corresponding index; maybe store a set of tuples (number, index)? This may not work because when I check the set of tuples, do I have to loop through the tuples?
create an empty set
loop through the list of nums
add each element and it's index as a tuple to the set
create a variable sum_two to store the difference of target - sum_one; when it is found, save the index of sum_one as index_one
check if sum_two is in the set of tuples as the second element in each tuple; when found, save it as index_two
return index_one, index_two
"""

# def twoSum(nums,target):
#     nums_index_dict = dict()
#     for i in range(len(nums)):
#         nums_index_dict[i] = nums_index_dict.get(nums[i])
#     print(nums_index_dict)


# print(twoSum([3,2,3],6))

# def twoSum(nums, target):
#     nums_index_dict = dict()
#     for i in range(len(nums)):
#         num = nums[i]
#         nums_index_dict[i] = num
#     # print(nums_index_dict)
#     for index in nums_index_dict:
#         if index == target - nums_index_dict[i]
#         if x in nums_index_dict:
#             return nums_index_dict[i], x

# print(twoSum([3, 2, 3], 6))

# working solution
# def twoSum(nums, target):
#     num_indices = {}  # Dictionary to store numbers and their indices
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_indices: # Check if the complement exists in the dictionary
#             return num_indices[complement], i # Return the indices of the two numbers
#         num_indices[num] = i # Add the current number and its index to the dictionary

# print(twoSum([3, 2, 3, 13,16,7,8,19,10], 12))
# working solution
# def twoSum(nums, target):
#     num_indices = {}  # Dictionary to store numbers and their indices
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_indices: # Check if the complement exists in the dictionary
#             return num_indices[complement], i # Return the indices of the two numbers
#         num_indices[num] = i # Add the current number and its index to the dictionary

# print(twoSum([3, 2, 3, 13,16,7,8,19,10], 12))

# def twoSum(nums, target):
#     num_indices = {}  # Dictionary to store numbers and their indices
    
#     for n in nums:
#         i = nums.index(n)
#         num_indices[i] = num_indices.get(i,n)
#         answer = target - n
        # if answer in num_indices.values(): 
#         print(num_indices[n])
#             # return num_indices[answer], i

# getting a key error
# print(twoSum([3, 2, 3, 13,16,7,8,19,10], 12))

def twoSum(nums, target):
    num_indices = {}  # Dictionary to store numbers and their indices
    
    for i, num in enumerate(nums):
        num_indices[num] = i
    print(num_indices) #  output {3: 2, 2: 1, 13: 3, 16: 4, 7: 5, 8: 6, 19: 7, 10: 8} why is the index of the first key 2, instead of 0? 
    
    # for num in nums:
    #     complement = target - num
    #     if complement in num_indices and num_indices[complement] != num_indices[num]:
    #         return num_indices[complement], num_indices[num]
    
    # return None

print(twoSum([3, 2, 3, 13, 16, 7, 8, 19, 10], 12))
