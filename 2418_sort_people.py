"""
2418. Sort the People

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Example 1:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
 

Constraints:
n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.

add the names and heights a dict name as the key, height as the value
loop through the dict and find the max height value, then output the key into a new list, continue until there are no more values
"""

# def sortPeople(names,heights):

names = ["Mary","John","Emma"]
heights = [180,165,170]

max = float('inf')
current_name = ''
ordered_heights = []

# for i in range(len(names)):
for i in range(len(heights)):
    if int(heights[i]) < max:
        current_max = int(heights[i])
    
    ordered_heights.append(names[i])

print(ordered_heights)

people = list()
for i in range(len(names)):
        people.append((names[i],heights[i]))
# print(name_ht_lst_tuples)

results = []
sorted_people = people.sorted(people[1])
print(sorted_people)