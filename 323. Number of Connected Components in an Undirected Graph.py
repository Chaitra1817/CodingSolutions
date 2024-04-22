'''
323. Number of Connected Components in an Undirected Graph
Solved
Medium
Topics
Companies

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)

        for i in edges:
            u,v=i
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    dfs(neigh)


        visited=set()
        res=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        
        return res

