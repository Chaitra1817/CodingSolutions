'''
103. Binary Tree Zigzag Level Order Traversal
Solved
Medium
Topics
Companies

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

'''

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        results = []
        q = deque([root])
        left_to_right = True
        
        while q:
            level_size = len(q)
            current_values = []
            
            for _ in range(level_size):
                if left_to_right:
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    node = q.pop()
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                
                current_values.append(node.val)
            
            results.append(current_values)
            left_to_right = not left_to_right

        return results
