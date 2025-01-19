'''
3427. Sum of Variable Length Subarrays
Solved
Easy
Companies
Hint

You are given an integer array nums of size n. For each index i where 0 <= i < n, define a
subarray
nums[start ... i] where start = max(0, i - nums[i]).

Return the total sum of all elements from the subarray defined for each index in the array.

 

Example 1:

Input: nums = [2,3,1]

Output: 11

Explanation:
i	Subarray	Sum
0	nums[0] = [2]	2
1	nums[0 ... 1] = [2, 3]	5
2	nums[1 ... 2] = [3, 1]	4
Total Sum	 	11

The total sum is 11. Hence, 11 is the output.

'''
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            ans+=sum(nums[start:i+1])
        return ans
        
