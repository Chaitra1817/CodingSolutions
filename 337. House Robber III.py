'''
337. House Robber III
Solved
Medium
Topics
Companies

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:

Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    0 <= Node.val <= 104

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def find(node, canPick):
            if not node:
                return 0

            # Check memo to see if we already computed the result for this node and state
            if (node, canPick) in memo:
                return memo[(node, canPick)]

            if canPick:
                # If we pick this node, we cannot pick its children
                take = node.val
                if node.left:
                    take += find(node.left, False)
                if node.right:
                    take += find(node.right, False)
            else:
                take = 0  # We can't take this node's value

            # Whether we pick this node or not, we can decide to pick or not pick its children
            notTake = find(node.left, True) + find(node.right, True)

            # Store the result in memo before returning
            result = max(take, notTake)
            memo[(node, canPick)] = result
            return result

        return find(root, True)

