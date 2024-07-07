'''
875. Koko Eating Bananas
Solved
Medium
Topics
Companies

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateTotalHours(piles, hourly):
            totalH = 0
            n = len(piles)
            # Find total hours
            for i in range(n):
                totalH += math.ceil(piles[i] / hourly)
            return totalH

        low = 1
        high = max(piles)
        ans=high

        while low <= high:
            mid = (low + high) // 2
            totalH = calculateTotalHours(piles, mid)
            if totalH <= h:
                high = mid - 1
                ans=mid
            else:
                low = mid + 1
        return ans
