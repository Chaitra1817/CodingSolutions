'''
652. Find Duplicate Subtrees
Medium
5.6K
443
company
Google
company
Bloomberg
company
TikTok

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Input: root = [2,1,1]
Output: [[1]]

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Merkel Trees 

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashmap = defaultdict(int)
        res = []
        
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                final_code = (node.val,left,right)

                if hashmap.get(final_code,0) == 1:
                    res.append(node)
                hashmap[final_code] += 1

                return final_code
            
            return -1
        
        dfs(root)
        return res 
