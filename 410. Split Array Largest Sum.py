'''
410. Split Array Largest Sum
Solved
Hard
Topics
Companies

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

'''
class Solution:
    def splitArray(self, a: List[int], k: int) -> int:
        def countPartitions(a, maxSum):
            n = len(a)  # size of array
            partitions = 1
            subarraySum = 0
            for i in range(n):
                if subarraySum + a[i] <= maxSum:
                    # insert element to current subarray
                    subarraySum += a[i]
                else:
                    # insert element to next subarray
                    partitions += 1
                    subarraySum = a[i]
            return partitions
            
        low = max(a)
        high = sum(a)
        while low <= high:
            mid = (low + high) // 2
            partitions = countPartitions(a, mid)
            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low

   





