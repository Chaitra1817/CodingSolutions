'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        
        def find(l,r):
            if not l and not r:
                return True
            if not l or not r :
                return False
            if l.val==r.val:
                return find(l.left, r.right) and find(l.right, r.left)
            else:
                return False
        
        return find(root.left,root.right)
        
