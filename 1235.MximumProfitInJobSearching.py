'''
1235. Maximum Profit in Job Scheduling
Solved
Hard
Topics
Companies
Hint

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

'''

from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])

        def findMax(ind, memo):
            nonlocal jobs
            if ind == len(jobs):
                return 0

            if ind in memo:
                return memo[ind]

            # Skip the current job
            notTake = findMax(ind + 1, memo)

            # Include the current job
            take = jobs[ind][2]
            nextJobIndex = self.findNextJob(ind, jobs)
            if nextJobIndex is not None:
                take += findMax(nextJobIndex, memo)

            # Calculate the maximum profit
            result = max(notTake, take)
            memo[ind] = result
            return result

        memo = {}
        return findMax(0, memo)

    def findNextJob(self, currentIdx, jobs):
        startTime = jobs[currentIdx][1]
        left, right = currentIdx + 1, len(jobs) - 1

        while left <= right:
            mid = (left + right) // 2
            if jobs[mid][0] >= startTime:
                right = mid - 1
            else:
                left = mid + 1

        if left < len(jobs):
            return left
        else:
            return None
