'''

Geek wants to know the traversals required to construct a unique binary tree. Given a pair of traversal, return true if it is possible to construct unique binary tree from the given traversals otherwise return false.

Each traversal is represented with an integer: preorder - 1, inorder - 2, postorder - 3.   

Example 1:

Input:
a = 1, b=2
Output: 1
Explanation: We can construct binary tree using inorder traversal and preorder traversal. 

'''

#User function Template for python3

class Solution:
    def isPossible(self, a, b):
        #Code here
        if (a, b) in [(1, 2), (2, 1), (2, 3), (3, 2)]:
            return True
        return False
