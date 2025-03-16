'''

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)

        ans=float('inf')
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                tmp=nums[i]+nums[l]+nums[r]
                if abs(target - tmp) < abs(target - ans):
                    ans = tmp
                if tmp==target:
                    return target
                elif tmp<target:
                    l+=1
                else:
                    r-=1
    
        return ans
