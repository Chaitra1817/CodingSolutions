'''
826. Most Profit Assigning Work
Solved
Medium
Topics
Companies

You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

    difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
    worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).

Every worker can be assigned at most one job, but one job can be completed multiple times.

    For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.

Return the maximum profit we can achieve after assigning the workers to the jobs.

 

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0

'''

from collections import defaultdict
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Create a dictionary to map difficulty to profit
        diffProfit = defaultdict(int)
        n = len(difficulty)
        
        # Populate the dictionary with maximum profit for each difficulty
        for i in range(n):
            diffProfit[difficulty[i]] = max(diffProfit[difficulty[i]], profit[i])
        
        # Ensure that for each difficulty, the profit is non-decreasing
        max_profit = 0
        for d in sorted(diffProfit):
            max_profit = max(max_profit, diffProfit[d])
            diffProfit[d] = max_profit
        
        # Sort the difficulty-profit pairs
        sorted_diff_profit = sorted(diffProfit.items(), key=lambda item: item[0])
        
        # Function to find the maximum profit for a given worker's ability
        def find_max_profit(ability):
            left, right = 0, len(sorted_diff_profit) - 1
            best_profit = 0
            while left <= right:
                mid = (left + right) // 2
                if sorted_diff_profit[mid][0] <= ability:
                    best_profit = sorted_diff_profit[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1
            return best_profit
        
        # Calculate the total maximum profit for all workers
        total_profit = 0
        for w in sorted(worker):
            total_profit += find_max_profit(w)
        
        return total_profit

