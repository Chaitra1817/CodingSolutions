'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

 

Constraints:

    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    There are no repeated edges.
    The given graph is connected.

'''

'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)

        def dfs(node,parent):
            visited.add(node)
            for neigh in adj[node]:
                if neigh==parent:
                    continue
                if neigh in visited:
                    return True
                if dfs(neigh,node):
                    return True
            
            return False

       
        adj=defaultdict(list)
        for u,v in edges:
            visited=set()
            adj[u].append(v)
            adj[v].append(u)
            if dfs(u,-1):
                return [u,v]
        
'''     

class Disjoinset:
    def __init__(self,n):
        self.rank=[0]*n
        self.parent=[i for i in range(n)]
    
    def find(self,k):
        if k!=self.parent[k]:
            self.parent[k]=self.find(self.parent[k])
        
        return self.parent[k]
    
    def union(self,u,v):
        ulpu=self.find(u)
        ulpv=self.find(v)

        if ulpu==ulpv:
            return True
        
        if self.rank[ulpu]>self.rank[ulpv]:
            self.parent[ulpv]=ulpu
        elif self.rank[ulpv]>self.rank[ulpu]:
            self.parent[ulpu]=ulpv
        else:
            self.parent[ulpv]=ulpu
            self.rank[ulpu]+=1
        
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        ds=Disjoinset(n+1)
        
        for u,v in edges:
            if ds.union(u,v):
                return [u,v]

        

        
