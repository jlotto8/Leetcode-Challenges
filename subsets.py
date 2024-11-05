"""
Subsets

Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [7]

Output: [[],[7]]
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10


solve with bitwise solution
solve recursively


"""

from typing import List        

def subsets(nums: List[int]) -> List[List[int]]:

    result = [[]]
        
    for num in nums:
        new_subsets = [] # temp list to hold new subsets
            
        # create a new subset by adding num to each subset in the current result
        for current_subset in result:
            new_subset = current_subset + [num] # copy the subset, add the number to it
            new_subsets.append(new_subset) # append the new subset
            
        result.extend(new_subsets) # add the new subset to the result
        
    return result

print(subsets([1,2,3]))



        