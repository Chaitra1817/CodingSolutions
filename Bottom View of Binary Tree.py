'''
Given a binary tree, return an array where elements represent the bottom view of the binary tree from left to right.

Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level traversal is considered. For example, in the below diagram, 3 and 4 are both the bottommost nodes at a horizontal distance of 0, here 4 will be considered.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree, the output should be 5 10 4 14 25.
'''
from collections import defaultdict, deque

class Solution:
    def bottomView(self, root):
        # code here
        
        d=defaultdict(int)
        ans=[]
        
        q=deque([(root,0)])
        
        while q:
            node,y=q.popleft()
            
            d[y]=node.data
            if node.left:
                q.append((node.left,y-1))
            if node.right:
                q.append((node.right,y+1))
        
        return [d[i] for i in sorted(d)]
