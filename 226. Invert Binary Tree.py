'''
226. Invert Binary Tree
Solved
Easy
Topics
Companies

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # right=self.invertTree(root.right)
        # left=self.invertTree(root.left)
        # root.left=right
        # root.right=left

        # return root

        #approach 2
        q=deque([root])

        while q:
            cur=q.popleft()
            cur.left, cur.right=cur.right, cur.left

            if cur.left:
                q.append(cur.left)
            
            if cur.right:
                q.append(cur.right)
            
        return root

