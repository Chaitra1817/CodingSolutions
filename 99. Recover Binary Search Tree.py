'''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first=second=prev=None
        def inorder(node):
            nonlocal first,second,prev
            if not node:
                return
            inorder(node.left)
            if prev and prev.val>node.val:
                if not first:
                    first=prev
                second=node
            prev=node
            inorder(node.right)

        
        inorder(root)
        if first and second:
            first.val,second.val=second.val,first.val
