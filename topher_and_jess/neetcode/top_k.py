"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

Hint 1
A naive solution would be to count the frequency of each number and then sort the array based on each element’s frequency. After that, we would select the top k frequent elements. This would be an O(nlogn) solution. Though this solution is acceptable, can you think of a better way?

Hint 2
Can you think of an algorithm which involves grouping numbers based on their frequency?

Hint 3
Use the bucket sort algorithm to create n buckets, grouping numbers based on their frequencies from 1 to n. Then, pick the top k numbers from the buckets, starting from n down to 1.

Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]
"""
def find_top_k(nums,k):

    num_freq = dict()
    for num in nums:
        if num in num_freq:
            num_freq[num] = num_freq[num] + 1
        else:
            num_freq[num] = 1
    pairs = list()

    for num, cnt in num_freq.items():
        pairs.append([cnt,num])
    pairs.sort()
    top_k = pairs[-k:]
    res = []
    for pair in reversed(top_k):
        res.append(pair[1])
    return res

# print(find_top_k(nums = [1,2,2,3,3,3], k = 2)) 

from collections import Counter

def top_k_frequent(nums, k):
    # return [num for num, freq in sorted(Counter(nums).items(), key=lambda x: -x[1])[:k]]
    return [x[0] for x in sorted(Counter(nums).items(), key=lambda x: -x[1])[:k]]

print(find_top_k(nums = [1,2,2,3,3,3], k = 2))

nums = [1,2,2,3,3,3]
counts = Counter(nums)

pairs = counts.items()
comp_freq_reverse = lambda pair: -pair[1]
sorted_pairs = 
