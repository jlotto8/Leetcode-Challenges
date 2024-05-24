"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 
Constraints
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self,value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            print('error')
        
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else: 
            print('error')

root = BinaryTree(3)
root.insert_left(9)
root.insert_right(20)

root.right_child.insert_right(7)
root.left_child.insert_left(15)