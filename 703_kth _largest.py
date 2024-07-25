"""
703. Kth Largest Element in a Stream
Solved
Easy
Topics
Companies
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

class Heap:
    def __init__(self, nodes, compare):
        """
        Initialize the heap with a list of nodes and a comparison function. The comparison function determines min-heap or max-heap.
        :param nodes: List of initial nodes to add to the heap.
        :param compare: Comparison function to maintain the heap property.
                        For a min-heap, use lambda x, y: x < y.
                        For a max-heap, use lambda x, y: x > y.
        """
        self.nodes = []  # Initialize an empty list to store heap elements
        self.compare = compare  # Store the comparison function

        for node in nodes:
            self.add(node)  # Add each node from the input list to the heap

    def __len__(self):
        return len(self.nodes) # Return the number of elements in the heap.

    def __get_left_child_index(self, parent_index):
        # Calculate the index of the left child of a given parent index. 
        # :param parent_index: Index of the parent node.
        # :return: Index of the left child.
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index):
        # Calculate the index of the right child of a given parent index.
        # :param parent_index: Index of the parent node.
        # :return: Index of the right child.
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index):
        # Calculate the index of the parent of a given child index.
        # :param child_index: Index of the child node.
        # :return: Index of the parent.
        return (child_index - 1) // 2

    def __has_left_child(self, parent_index):
        # Check if a given parent index has a left child.
        # :param parent_index: Index of the parent node.
        # :return: True if the parent has a left child, False otherwise.
        return self.__get_left_child_index(parent_index) < len(self.nodes)

    def __has_right_child(self, parent_index):
        # Check if a given parent index has a right child.
        # :param parent_index: Index of the parent node.
        # :return: True if the parent has a right child, False otherwise.
        return self.__get_right_child_index(parent_index) < len(self.nodes)

    def __has_parent(self, index):
        # Check if a given index has a parent. The root node does not have a parent.
        # :param index: Index of the node.
        # :return: True if the node has a parent, False otherwise.
        # return self.__get_parent_index(index) >= 0
        return index != 0  
    

    def __swap(self, first_index, second_index):
        """
        Swap the elements at two given indices in the heap.
        :param first_index: Index of the first element.
        :param second_index: Index of the second element.
        """
        if first_index >= len(self.nodes) or second_index >= len(self.nodes):
            raise IndexError(f'first ({first_index}) or second ({second_index}) are invalid')
        self.nodes[first_index], self.nodes[second_index] = self.nodes[second_index], self.nodes[first_index]

        """
        Adding/inserting
        Get the element (starting with the last one)
        Check if it disobeys the priority rule, check if its value is smaller than the parent
        If smaller, then swap with its parent
        Recurse in the index of the parent
        Keep bubbling up/sifting up until reaching the root
        """
    
    def __heapify_up(self, child=None):
        # Maintain the heap property by moving the last added element up to its correct position.
        # :param child: Index of the element to heapify up. If None, starts with the last element.
        if child is None:
            # If no specific child index is provided, start with the last element in the heap
            child = len(self.nodes) - 1
        # Get the index of the parent of the current child
        parent_idx = self.__get_parent_index(child)
        
        # Continue swapping the child with its parent while the child violates the heap property
        # The loop runs as long as the child has a parent and the child should be "higher" (based on compare function) than the parent
        while self.__has_parent(child) and self.compare(self.nodes[child], self.nodes[parent_idx]):
            # Swap the positions of the child and its parent
            self.__swap(child, parent_idx)
            # Update the child's index to the parent's index (since they were swapped)
            child = parent_idx
            # Get the new parent's index for the updated child index
            parent_idx = self.__get_parent_index(child)


    def add(self, item):
        # Add an element to the heap and maintain the heap property.  :param item: Element to be added to the heap.
        self.nodes.append(item)  # Append the new item to the end of the list
        self.__heapify_up()  # Move the new item to its correct position in the heap

        """
    Deleting
    Get the element key (starts with the first element)
    Check if the key is greater than any of the children (left or right)
    If greater, than it is in the wrong position, swap with the smallest between left and right
    Continue to heapify down with the smallest child index
    Repeat until no more children
        """

    def __heapify_down(self, index=0):
        """
        Maintain the heap property by moving the root element down to its correct position.
        :param index: Index of the element to heapify down. Defaults to the root element.
        """
        # Continue as long as the current node has at least one left child
        while self.__has_left_child(index):
            # Assume the left child is the smaller child initially
            smaller_child_idx = self.__get_left_child_index(index)
            
            # If the right child exists and is "higher" (based on compare function) than the left child
            if self.__has_right_child(index) and self.compare(self.nodes[self.__get_right_child_index(index)], self.nodes[smaller_child_idx]):
                # Update smaller_child_idx to the right child's index
                smaller_child_idx = self.__get_right_child_index(index)
            
            # If the current node is in the correct position relative to its children, break the loop
            if self.compare(self.nodes[index], self.nodes[smaller_child_idx]):
                break

            # Swap the current node with the smaller child
            self.__swap(index, smaller_child_idx)
            # Update the index to the smaller child's index to continue heapifying down
            index = smaller_child_idx

        """
        Removing the minimum element
        Polls lowest element from the heap. To avoid memory shift
        of first-element removal, copy the last element to the first
        position, shrink the size by 1 and heapify down.
        """
    
    def poll(self):
        # Remove and return the top element (minimum for MinHeap, maximum for MaxHeap) from the heap. return: The removed top element.
        if not self.nodes:
            return None

        removed_node = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()  # Remove the last element
        self.__heapify_down()  # Move the new root element to its correct position in the heap
        return removed_node

    def peek(self):
        # Return the top element (minimum for MinHeap, maximum for MaxHeap) without removing it. return: The top element of the heap.
        if not self.nodes:
            return None
        return self.nodes[0]

# Create MinHeap and MaxHeap classes by passing the appropriate comparison function
class MinHeap(Heap):
    def __init__(self, nodes):
        # Initialize a MinHeap with a list of nodes. param nodes: List of initial nodes to add to the heap.
        super().__init__(nodes, compare=lambda x, y: x < y)

class MaxHeap(Heap):
    def __init__(self, nodes):
        # Initialize a MaxHeap with a list of nodes. param nodes: List of initial nodes to add to the heap.
        super().__init__(nodes, compare=lambda x, y: x > y)

class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k  # Store the k value
        self.min_heap = MinHeap([])  # Initialize an empty MinHeap
        
        # Add each number from the initial stream to the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.min_heap.add(val)  # Add the new value to the heap
        
        # If the heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            self.min_heap.poll()
        
        # The kth largest element is the smallest element in the MinHeap
        return self.min_heap.peek()
    
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(5))  # Output: 5
print(kthLargest.add(10))  # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8