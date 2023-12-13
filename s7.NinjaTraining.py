#Memoization
from typing import List

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    memo = [[-1 for _ in range(4)] for _ in range(n)]  

    def findMax(row, task):
        if row < 0:
            return 0
        if memo[row][task] != -1:
            return memo[row][task]

        max_points = 0
        for i in range(3):
            if i != task:
                new_val = points[row][i] + findMax(row - 1, i)
                max_points = max(max_points, new_val)

        memo[row][task] = max_points
        return max_points

    return findMax(n - 1, 3)

