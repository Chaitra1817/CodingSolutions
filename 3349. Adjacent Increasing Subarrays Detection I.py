'''

Given an array nums of n integers and an integer k, determine whether there exist two adjacent
subarrays
of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:

    Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
    The subarrays must be adjacent, meaning b = a + k.

Return true if it is possible to find two such subarrays, and false otherwise.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1], k = 3

Output: true

Explanation:

    The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
    The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
    These two subarrays are adjacent, so the result is true.

Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7], k = 5

Output: false

'''

from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # We need two adjacent subarrays of length `k`, so t should go up to `n - 2 * k`.
        for t in range(n - 2 * k + 1):
            found1, found2 = True, True
            
            # Check if the first subarray nums[t:t+k] is strictly increasing
            for i in range(t, t + k - 1):
                if nums[i] >= nums[i + 1]:
                    found1 = False
                    break
            
            # Check if the second subarray nums[t+k:t+2*k] is strictly increasing
            for j in range(t + k, t + 2 * k - 1):
                if nums[j] >= nums[j + 1]:
                    found2 = False
                    break
            
            # If both subarrays are found to be strictly increasing, return True
            if found1 and found2:
                return True

        # If no such pair of subarrays is found, return False
        return False
