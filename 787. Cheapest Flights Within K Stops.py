'''

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700

'''

from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))

        total = [float('inf')] * n
        total[src] = 0

        q = deque([(0, 0, src)])
        
        while q:
            stops, costSoFar, node = q.popleft()
            
            if stops <= k:
                for neighbor, price in adj[node]:
                    newCost = costSoFar + price
                    if newCost < total[neighbor]:
                        total[neighbor] = newCost
                        q.append((stops + 1, newCost, neighbor))

        return total[dst] if total[dst] != float('inf') else -1
