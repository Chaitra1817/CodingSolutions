'''
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

    The items that belong to the same group are next to each other in the sorted list.
    There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).

Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]

Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

 

Constraints:

    1 <= m <= n <= 3 * 104
    group.length == beforeItems.length == n
    -1 <= group[i] <= m - 1
    0 <= beforeItems[i].length <= n - 1
    0 <= beforeItems[i][j] <= n - 1
    i != beforeItems[i][j]
    beforeItems[i] does not contain duplicates elements.

'''

from typing import List
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        G = m
        for i in range(n):
            if group[i] == -1:
                group[i] = G
                G += 1

        grp = defaultdict(list)
        indegree_grp = [0] * G

        item = defaultdict(list)
        indegree_item = [0] * n

        for i in range(n):
            for k in beforeItems[i]:
                item[k].append(i)
                indegree_item[i] += 1

                gu, gv = group[k], group[i]
                if gu != gv:
                    grp[gu].append(gv)
                    indegree_grp[gv] += 1

        def find(adj, indegree, size):
            q = deque([])
            for i in range(size):
                if indegree[i] == 0:
                    q.append(i)

            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for neigh in adj.get(node, []):
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)

            return order if len(order) == size else []

        gp_order = find(grp, indegree_grp, G)
        if not gp_order:
            return []

        item_order = find(item, indegree_item, n)
        if not item_order:
            return []

        sorted_orer = defaultdict(list)
        for it in item_order:
            sorted_orer[group[it]].append(it)

        ans = []
        for g in gp_order:
            ans.extend(sorted_orer[g])

        return ans if len(ans) == n else []


'''
TC: O(n + E)

SC: O(n + E)

'''
