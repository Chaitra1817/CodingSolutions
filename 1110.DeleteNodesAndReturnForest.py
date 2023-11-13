"""
1110. Delete Nodes And Return Forest
Medium
3.7K
104
company
Google
company
Facebook
company
Amazon

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        store=[]
        def deleteNode(root,store):
            if root is None:
                return None
    
            root.left=deleteNode(root.left,store)
            root.right=deleteNode(root.right,store)
            if root.val in to_delete:
                if root.left:
                    store.append(root.left)
                if root.right:
                    store.append(root.right)
                return None
            return root           
        deleteNode(root,store)
        if root.val not in to_delete:
            store.append(root)
        return store
