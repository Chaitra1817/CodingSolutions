'''
236. Lowest Common Ancestor of a Binary Tree
Solved
Medium
Topics
Companies

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None

        def find(node):
            # Base case: if the node is None or matches p or q, return the node.
            if not node or node == p or node == q:
                return node

            # Recursively search in the left and right subtrees.
            left = find(node.left)
            right = find(node.right)

            # If both left and right return non-None, this node is the LCA.
            if left and right:
                return node

            # Otherwise, return the non-None result, or None if both are None.
            return left if left else right

        # Start the search from the root.
        return find(root)

