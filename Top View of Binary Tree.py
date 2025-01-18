'''
You are given a binary tree, and your task is to return its top view. The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note: 

    Return the nodes from the leftmost node to the rightmost node.
    If two nodes are at the same position (horizontal distance) and are outside the shadow of the tree, consider the leftmost node only. 

Examples:

Input: root[] = [1, 2, 3] 
 
Output: [2, 1, 3]

'''

from collections import defaultdict, deque

class Solution:
    # Function to return a list of nodes visible from the top view
    # from left to right in a Binary Tree.
    def topView(self, root):
        if not root:
            return []

        # Dictionary to store the first node at each horizontal distance (hd)
        d = {}

        # Queue for level-order traversal; stores pairs of node and hd
        q = deque([(root, 0)])

        while q:
            node, hd = q.popleft()

            # Add to dictionary only if hd is not already present
            if hd not in d:
                d[hd] = node.val

            # Traverse left and right subtrees
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        # Extract values in sorted order of hd
        return [d[key] for key in sorted(d.keys())]
