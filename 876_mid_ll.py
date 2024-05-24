"""
876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

"""

import typing
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
         fast = head
         
         for slow in range(len(head)):
             if fast == len(head):
                 




# practice return middle of regular list
# [1,2,3,4,5]

# def mid_list(nums):
     
#     fast = 0


#     for slow in range(len(nums)):
#         # print(f'slow pointer index = {slow} and element = {nums[slow]}')
#         # print(f'fast pointer index = {fast} and element = {nums[fast]}')
#         # print(f'fast = {fast},fast +1 = {fast +1}, length of nums = {len(nums)}')
#         if fast +1 == len(nums):
#             return nums[slow]
#         fast += 2
#     return None
# print(mid_list([1,2,3,4,5]))
               