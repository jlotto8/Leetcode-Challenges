# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         self.nums= nums
#         self.target = target
#         sum_of_two_ints = 0
#         list_of_indices = []
#         for i in range(nums):
#             for j in range(nums):
#                 print(i,j[1])
#                 sum_of_two_ints += i+j
#         print(sum_of_two_ints)
#         if target == sum_of_two_ints:
#             list_of_indices = [i,j].append
#         print(list_of_indices)
#         return list_of_indices
#     twoSum([0,1,9,2],10)
        
        # O: List of 2 indices of two integers that add up to the target
        # I: List of integers nums, and an integer called Target- which two integers add up to
        # C: Each input will have 1 solution. You may not use the same element twice You can return the answer in any order  
        # 2 <= nums.length <= 10^4  -10^9 <= nums[i] <= 10^9-10^9 <= target <= 10^9 Only one valid answer exists.
        # E: none
# Pseudocode:
# create an accumulator called sum
# create an empty list to hold the indices that will be returned as the ouput 
# loop through the list of integers for i in range(len(nums)):
    # loop through again for j in range(len(nums)): #QUESTION what happens if for j in range(len(nums(1,-1)))
    # starting at index 1 instead of 0 so that the same element is not used twice add each integer to the next one sum = sum +j+i
# if target == i+j QUESTION if target == sum?
    # add the index of i and j to the list
# return the list
# nums = [0,1,9]
# target = 10
# list_of_indices = []
# for i in range(len(nums)):
#     print(i)
#     for j in range(len(nums)):
#         j = i+1
#     print(i,j)
# if target == i+j:
#     list_of_indices.append([i],[j])
#     print(list_of_indices)
    # return list_of_indices
# expected ouput [1,2]

def twonumbersum(list, targetsum):
  list_of_ints= []
  for i in range(len(list)): 
    for j in range(i+1, len(list)):
      if list[i] + list[j] == targetsum: # QUESTION why not if targetsum == list[i] + list[j]??
        list_of_ints.append(list[i]) # QUESTION why not list_of_ints.append([i])?
        list_of_ints.append(list[j])
        print(list_of_ints)
          
  return list_of_ints
  
  
twonumbersum(list=[3,5,-4,8,11,1,-1,6],targetsum=10)
# ([3, 5, -4, 8, 11, 1, -1, 6], 10)