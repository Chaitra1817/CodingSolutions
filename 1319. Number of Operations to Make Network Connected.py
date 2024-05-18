'''
1319. Number of Operations to Make Network Connected
Solved
Medium
Topics
Companies
Hint

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

'''

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset==yset:
            return
        if self.size[xset] < self.size[yset]:
            self.parent[xset] = yset
            self.size[yset]+=self.size[xset]
        else:
            self.parent[yset] = xset
            self.size[xset]+=self.size[yset]
 

class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        dsu = UnionFind(n)
        number_of_connected_components = n

        for connection in connections:
            if dsu.find(connection[0]) != dsu.find(connection[1]):
                number_of_connected_components -= 1
                dsu.union_set(connection[0], connection[1])

        return number_of_connected_components - 1
