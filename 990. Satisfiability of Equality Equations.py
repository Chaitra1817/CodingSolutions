'''
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

 

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

 

Constraints:

    1 <= equations.length <= 500
    equations[i].length == 4
    equations[i][0] is a lowercase letter.
    equations[i][1] is either '=' or '!'.
    equations[i][2] is '='.
    equations[i][3] is a lowercase letter.

'''

class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]

    def find(self, k):
        if k != self.parent[k]:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def union(self, u, v):
        ulpu = self.find(u)
        ulpv = self.find(v)
        if ulpu == ulpv:
            return False

        if self.rank[ulpu] < self.rank[ulpv]:
            self.parent[ulpu] = ulpv
        elif self.rank[ulpv] < self.rank[ulpu]:
            self.parent[ulpv] = ulpu
        else:
            self.parent[ulpv] = ulpu
            self.rank[ulpu] += 1
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ds = DisjointSet(26)  

        for eq in equations:
            if eq[1:3] == "==":
                u = ord(eq[0]) - ord('a')
                v = ord(eq[3]) - ord('a')
                ds.union(u, v)

        for eq in equations:
            if eq[1:3] == "!=":
                u = ord(eq[0]) - ord('a')
                v = ord(eq[3]) - ord('a')
                if ds.find(u) == ds.find(v):
                    return False

        return True
