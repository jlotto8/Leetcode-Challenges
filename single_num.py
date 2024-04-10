"""
I: list of integers
O: one integer
C:1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
E: more than 2 of the same number?
the list has two of every number, except for one number
go through the list
if element in list == any other element in the list
    remove  it
return the remaining element in the list

for i in nums:
    if i == i+1:
        nums.remove[i]
    return nums
        for i in nums:
            for j in nums:
                if i == j:
                    nums.remove(i)
                    nums.remove(j)
                return nums[0]
"""
# class Solution:
# def singleNumber(nums):
nums = [2,2,1]

while len(nums) > 1:

    for i in range(len(nums)):
        for j in range(i+1,nums):
            if i == j:
                nums.remove(i)
                nums.remove(j-1)
        print(nums)


# s = set()
# for i in set(nums):
#     if nums.count(i) == 1:
#         print(i)