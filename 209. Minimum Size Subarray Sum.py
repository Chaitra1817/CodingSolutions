'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a

whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

 

Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,0
        ans=float('inf')
        total=0
        while r<n:
            total+=nums[r]
            
            while total>=target:
                ans=min(ans,r-l+1)
                total-=nums[l]
                l+=1

            r+=1
        
        return ans if ans!=float('inf') else 0
