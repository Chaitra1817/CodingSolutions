'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 109
    All the integers in nums are unique.

'''


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n

        max_size = 0
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        ans = []
        while max_index != -1:
            ans.append(nums[max_index])
            max_index = prev[max_index]

        return ans

# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         nums.sort()  
#         dp = {}

#         def find(idx, res):
#             if idx == len(nums):
#                 return res  

#             if (idx, tuple(res)) in dp:  
#                 return dp[(idx, tuple(res))]

#             notTake = find(idx + 1, res) 
#             take = []
#             if res == [] or nums[idx] % res[-1] == 0:
#                 take = find(idx + 1, res + [nums[idx]])

#             dp[(idx, tuple(res))] = max(notTake, take, key=len)  
#             return dp[(idx, tuple(res))]

#         return find(0, [])
