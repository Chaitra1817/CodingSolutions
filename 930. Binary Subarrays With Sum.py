'''

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15

'''

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def find(target):
            if target<0:
                return 0
                
            l, r = 0, 0
            n = len(nums)
            total = 0
            cnt=0

            while r < n:
                total += nums[r]

                while total >target:  
                    total -= nums[l]
                    l += 1
                
                cnt+=r-l+1
                r += 1  
            
            return cnt
        return find(goal)-find(goal-1)





            


