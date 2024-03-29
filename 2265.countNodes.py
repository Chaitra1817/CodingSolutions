''''
2265. Count Nodes Equal to Average of Subtree
Medium
2K
35
company
Google
company
Facebook
company
Amazon

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

    The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
    A subtree of root is a tree consisting of root and all of its descendants.

Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation: 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def postOrder(root):
            
            if root is None:
                return(0,0)
            left=postOrder(root.left)
            right=postOrder(root.right)
            print("left",left)
            print("right",right)
            nodeSum=left[0]+right[0]+root.val
            nodeCount=left[1]+right[1]+1
            print("nodesum",nodeSum,nodeCount)
            print("roo",root.val)
            if nodeSum//nodeCount==root.val:
                nonlocal ans
                ans+=1
                print("ans",ans)

            return (nodeSum,nodeCount)

        postOrder(root)
        return(ans)




   






