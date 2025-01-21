'''
Given a binary tree having n nodes. Check whether all of its nodes have a value equal to the sum of their child nodes. Return 1 if all the nodes in the tree satisfy the given properties, else it returns 0. For every node, the data value must be equal to the sum of the data values in the left and right children. Consider the data value 0 for a NULL child. Also, leaves are considered to follow the property.

Examples:

Input:
Binary tree
       35
      /  \
     20   15
    / \   / \
   15  5 10  5

Output: 1
Explanation: 
Here, every node is sum of its left and right child.

'''

#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        if not root:
            return 1
        
        def find(node):
            if not node:
                return 0 
            
            if not node.left and not node.right:
                return node.data
            
            left = find(node.left)
            right = find(node.right)
            
            # If any subtree violates the property, propagate failure
            if left == -1 or right == -1 or node.data != (left + right):
                return -1  # Indicating the property is violated
            
            return node.data
        
        return 1 if find(root) != -1 else 0

