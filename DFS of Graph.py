'''
Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Traversal (DFS) starting from vertex 0, visiting vertices from left to right as per the adjacency list, and return a list containing the DFS traversal of the graph.

Note: Do traverse in the same order as they are in the adjacency list.

Examples:

Input: adj = [[2,3,1], [0], [0,4], [0], [2]]

Output: [0, 2, 4, 3, 1]
Explanation: Starting from 0, the DFS traversal proceeds as follows: 
Visit 0 → Output: 0 
Visit 2 (the first neighbor of 0) → Output: 0, 2 
Visit 4 (the first neighbor of 2) → Output: 0, 2, 4 
Backtrack to 2, then backtrack to 0, and visit 3 → Output: 0, 2, 4, 3 
Finally, backtrack to 0 and visit 1 → Final Output: 0, 2, 4, 3, 1

Input: adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

Output: [0, 1, 2, 3, 4]
Explanation: Starting from 0, the DFS traversal proceeds as follows: 
Visit 0 → Output: 0 
Visit 1 (the first neighbor of 0) → Output: 0, 1 
Visit 2 (the first neighbor of 1) → Output: 0, 1, 2 
Visit 3 (the first neighbor of 2) → Output: 0, 1, 2, 3 
Backtrack to 2 and visit 4 → Final Output: 0, 1, 2, 3, 4

Constraints:
1 ≤ adj.size() ≤ 104
1 ≤ adj[i][j] ≤ 104
'''

from typing import List

class Solution:
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        ans = []
        visited = set()
        
        def find(node):
            if node in visited:  # Prevents revisiting nodes
                return
            visited.add(node)    # Mark node as visited
            ans.append(node)     # Add to result
            
            for neigh in adj[node]:  
                if neigh not in visited:
                    find(neigh)
        
        find(0)  # Start DFS from node 0
        return ans  # Return DFS traversal order
