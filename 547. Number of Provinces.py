'''
547. Number of Provinces
Solved
Medium
Topics
Companies

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        adj=defaultdict(set)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    adj[i].add(j)
                    adj[j].add(i)
        
        def dfs(node):
            visited.add(node)
            for neigh in list(adj[node]):
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)
        
        visited=set()
        cnt=0
        for i in range(len(adj)):
            if i not in visited:
                cnt+=1
                dfs(i)
        
        return cnt
