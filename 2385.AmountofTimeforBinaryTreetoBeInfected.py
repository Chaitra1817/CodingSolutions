'''
2385. Amount of Time for Binary Tree to Be Infected
Solved
Medium
Topics
Companies
Hint

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

    The node is currently uninfected.
    The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.

 

Example 1:

Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:

Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.





,,,

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj=defaultdict(list)
        def dfs(node):
            if node is None:
                return
            
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
            
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        visited=set()
        queue=deque([start])
        time=-1
        
        while queue:
            time+=1
            for _ in range(len(queue)):
                cur=queue.popleft()
                visited.add(cur)
                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return time
