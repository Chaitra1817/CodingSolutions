'''
501. Find Mode in Binary Search Tree
Solved
Easy
Topics
Companies

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.

 
Input: root = [1,null,2,2]
Output: [2]

Example 2:

Input: root = [0]
Output: [0]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        def postOrder(node):
            if node==None:
                return
            
            left=postOrder(node.left)
            right=postOrder(node.right)

            dic[node.val]=dic.get(node.val,0)+1
        
        postOrder(root)
        mx=max(dic.values())
        return [i for i in dic if dic[i]==mx]

