'''
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:

Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    Node.val == 0

'''
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        cameras = 0

        def find(node):
            nonlocal cameras
            if not node:
                return 1  # null nodes are considered watched

            l = find(node.left)
            r = find(node.right)

            # if any child is not watched, place camera here
            if l == 0 or r == 0:
                cameras += 1
                return 2  # has camera

            # if any child has camera, this node is watched
            if l == 2 or r == 2:
                return 1  # being watched

            # otherwise, not watched
            return 0

        # if root is not watched, add one camera
        if find(root) == 0:
            cameras += 1

        return cameras
