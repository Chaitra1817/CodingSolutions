'''

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        val=[]

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            val.append(node.val)
            inorder(node.right)

        
        inorder(root)

        seen = set()
        for num in val:
            if k - num in seen:
                return True
            seen.add(num)
        return False
