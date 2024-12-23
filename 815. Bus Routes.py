'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

'''
from collections import deque, defaultdict
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Step 1: Build the stop-to-routes mapping
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
        
        # Step 2: Initialize the BFS
        queue = deque([(source, 0)])  # (current stop, number of buses taken)
        visited_stops = set([source])
        visited_routes = set()
        
        while queue:
            current_stop, buses_taken = queue.popleft()
            
            # Explore all routes passing through the current stop
            for route in stop_to_routes[current_stop]:
                if route in visited_routes:
                    continue
                visited_routes.add(route)
                
                # Explore all stops in this route
                for stop in routes[route]:
                    if stop == target:
                        return buses_taken + 1
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, buses_taken + 1))
        
        return -1  
