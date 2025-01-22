'''
Given a binary tree and a node data called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.
Note: The tree contains unique values.

Examples : 

Input: root[] = [1,2,3,4,5,N,6,N,N,7,8,N,9,N,N,N,N,N,10],  target = 8
  
Output: 7
Explanation: If leaf with the value 8 is set on fire. 
After 1 sec: 5 catches fire.
After 2 sec: 2, 7 catches fire.
After 3 sec: 4, 1 catches fire.
After 4 sec: 3 catches fire.
After 5 sec: 6 catches fire.
After 6 sec: 9 catches fire.
After 7 sec: 10 catches fire.
It takes 7s to burn the complete tree.

Input: root[] = [1, 2, 3, 4, 5, N, 7, 8, N, 10], target = 10

Output: 5
Explanation: If leaf with the value 10 is set on fire. 
- After 1 sec: Node 5 catches fire.
- After 2 sec: Node 2 catches fire.
- After 3 sec: Nodes 1 and 4 catches fire.
- After 4 sec: Node 3 and 8 catches fire.
- After 5 sec: Node 7 catches fire.
It takes 5s to burn the complete tree.

Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105
Company Tags
'''

#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def minTime(self, root,target):
        # code here
        q=deque([(root,None)])
        d=defaultdict(list)
        while q:
            n=len(q)
            for i in range(n):
                node,parent=q.popleft()
                if parent:
                    d[node.data].append(parent.data)
                    d[parent.data].append(node.data)
                if node.left:
                    q.append((node.left,node))
                if node.right:
                    q.append((node.right,node))
        
        ans=0
        visited=set()
        q=deque([(target,0)])
        visited.add(target)
        while q:
            cur,cnt=q.popleft()
            for neighbor in d[cur]:
                if neighbor not in visited:
                    q.append((neighbor,cnt+1))
                    visited.add(neighbor)
            ans = max(ans, cnt)
        return ans
            
