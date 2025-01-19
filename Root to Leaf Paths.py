'''
Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Note: The paths should be returned such that paths from the left subtree of any node are listed first, followed by paths from the right subtree.

Examples:

Input: root[] = [1, 2, 3, 4, 5]
ex-3
Output: [[1, 2, 4], [1, 2, 5], [1, 3]] 
Explanation: All possible paths: 1->2->4, 1->2->5 and 1->3

'''


from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root):
        if not root:
            return []

        ans = []

        def find(node, temp):
            if not node:
                return

            temp.append(node.data)

            if not node.left and not node.right:
                ans.append(list(temp))
            else:
                find(node.left, temp)
                find(node.right, temp)

            temp.pop()

        find(root, [])
        return ans

