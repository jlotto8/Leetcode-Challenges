"""
234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert_at_beginning(self):
        if self.head is None:
            ListNode.head = 1
            ListNode.next = 2


