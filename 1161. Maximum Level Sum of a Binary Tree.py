'''
1161. Maximum Level Sum of a Binary Tree
Solved
Medium
Topics
Companies
Hint

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

'''
from collections import deque
import sys

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        cur_level = 0
        max_sum = -sys.maxsize
        max_level = 0
        
        while q:
            cur_level += 1
            level_sum = 0
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                if node:
                    level_sum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            # Update the maximum sum and the level at which it occurs
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = cur_level
        
        return max_level
