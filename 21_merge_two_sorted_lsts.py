"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

dummy node?

complete with 2 arrays first
list1 = [1,2,4], list2 = [1,3,4]
"""

def merge_2_sorted_lists(list1, list2):

    list3 = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] < list2[j]:
                list3.append(list1[i])
            elif list1[i] > list2[j]:
                list3.append(list2[j])

# how to change incrementation




# def merge_2_sorted_lists(list1, list2):

#     i = 0
#     j = 0
#     merged_lst = []

#     while  i < len(list1) and j <len (list2):
#         if list1[i] < list2[j]:
#             merged_lst.append(list1[i])
#             i += 1
#         else:
#             merged_lst.append(list2[j])
#             j +=1

#     while i < len(list1):
#         merged_lst.append(list1[i])
#         i += 1
#     while i < len(list2):
#         merged_lst.append(list2[j])
#         j += 1
#     return merged_lst
        
# print(merge_2_sorted_lists([1,2,4],[1,3,4]))
