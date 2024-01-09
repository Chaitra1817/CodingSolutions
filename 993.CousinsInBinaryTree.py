'''
993. Cousins in Binary Tree
Solved
Easy
Topics
Companies

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def traverse(node, find, h, parent):
            if not node:
                return (0, -1)  
            if node.val == find:
                return (h, parent)

            left_depth, left_parent = traverse(node.left, find, h + 1, node.val)
            right_depth, right_parent = traverse(node.right, find, h + 1, node.val)

            return (left_depth or right_depth, left_parent if left_depth else right_parent)

        x_depth, x_parent = traverse(root, x, 0, -1)
        y_depth, y_parent = traverse(root, y, 0, -1)


        return x_depth == y_depth and x_parent != y_parent
