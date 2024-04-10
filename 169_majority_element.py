from collections import Counter

def majorityElement(nums):

    num_count = Counter(nums)
    return num_count.most_common(0)[1]

print(majorityElement(nums =[3,3,2]))