'''

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''

# Memoization
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        memo={}
        ans=False
        def find(idx):
            nonlocal ans
            if idx==n-1:
                return True

            if idx>=n:
                return False
            
            if idx in memo:
                return memo[(idx)]

            k=nums[idx]
            for i in range(k,0,-1):
                ans=find(idx+i)
                if ans:
                    break

            memo[(idx)]=ans
            return memo[(idx)]    
            
        return find(0)


# Tabulation

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True  

        for i in range(1, n):
            for j in range(i-1,-1,-1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break  

        return dp[-1]
