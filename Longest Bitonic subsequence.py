'''
Given an array of positive integers. Find the maximum length of Bitonic subsequence. 
A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing. Return the maximum length of bitonic subsequence.
 
Note : A strictly increasing or a strictly decreasing sequence should not be considered as a bitonic sequence

Examples :

Input: n = 5, nums[] = [1, 2, 5, 3, 2]
Output: 5
Explanation: The sequence {1, 2, 5} is increasing and the sequence {3, 2} is decreasing so merging both we will get length 5.

Input: n = 8, nums[] = [1, 11, 2, 10, 4, 5, 2, 1]
Output: 6
Explanation: The bitonic sequence {1, 2, 10, 4, 2, 1} has length 6.

Input: n = 5, nums[] = [10, 20, 30]
Output: 0
Explanation: The decreasing or increasing part cannot be empty

Input: n = 3, nums[] = [10, 10, 10]
Output: 0
Explanation: The subsequences must be strictly increasing or decreasing

Constraints:
1 ≤ length of array ≤ 103
1 ≤ arr[i] ≤ 104

'''


from typing import List

class Solution:
    def LongestBitonicSequence(self, n : int, nums : List[int]) -> int:
        # code here
        dp1 = [1] * n
        dp2 = [1] * n
        ans = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp1[j]+1>dp1[i]:
                    dp1[i] = max(dp1[i], dp1[j] + 1)
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[i]>nums[j] and dp2[j]+1>dp2[i]:
                    dp2[i] = max(dp2[i], dp2[j] + 1)
        
        max_length = 0
        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:  
                max_length = max(max_length, dp1[i] + dp2[i] - 1)

        return max_length
