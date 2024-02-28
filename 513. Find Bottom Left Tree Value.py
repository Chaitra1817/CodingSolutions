'''
513. Find Bottom Left Tree Value
Solved
Medium
Topics
Companies

Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:

Input: root = [2,1,3]
Output: 1

Example 2:

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        leftmost_value = None
        max_depth = -1

        def dfs(node, depth):
            nonlocal leftmost_value, max_depth
            if not node:
                return

            if depth > max_depth:
                leftmost_value = node.val
                max_depth = depth

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return leftmost_value

