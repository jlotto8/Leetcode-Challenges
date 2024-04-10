# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_prefix(list):

    result = ''

    for i in range(len(list)):
        # print(list[i])
        for j in range(len(list)):
            # print(list[i])
            print(list[i])



longest_prefix(list=['flowers', 'flow', 'flight'])