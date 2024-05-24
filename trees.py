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


        # [3,9,20,null,null,15,7]
print(root.value)
# print values given only the root node
# BFS, queue
# FIFO
# add root to queue
# depth of root = 1
# binary trees have 2 max children; keep track of depth, each level has a depth increase of 1
queue = []
# (root, 1) (node,depth of node)
maxdepth = 0
while queue:
    
    # remove the first item in queue
    # print it, complete operation
    # if there is a child, add to queue for left and right
    # add 1 to the depth, add it and the node value to the queue
    # keep track of max depth

# try DFS with recursion
# write out function calls
# 