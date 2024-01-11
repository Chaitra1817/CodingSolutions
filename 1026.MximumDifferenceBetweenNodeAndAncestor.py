'''
1026. Maximum Difference Between Node and Ancestor
Solved
Medium
Topics
Companies
Hint

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def findMax(node,ans,mx,mn):
            if node is None:
                return
            
            mx=max(mx,node.val)
            mn=min(mn,node.val)
            ans[0]=max(ans[0],abs(mx-mn))

            left=findMax(node.left,ans,mx,mn)
            right=findMax(node.right,ans,mx,mn)
            
            return
        
        ans=[float('-inf')]
        findMax(root,ans,root.val,root.val)
        return ans[0]
            
        
