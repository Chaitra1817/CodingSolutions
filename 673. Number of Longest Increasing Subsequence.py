'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

 

Constraints:

    1 <= nums.length <= 2000
    -106 <= nums[i] <= 106
    The answer is guaranteed to fit inside a 32-bit integer.

'''

# class Solution:
#     def findNumberOfLIS(self, nums):
#         n = len(nums)
#         length = [0] * n
#         count = [0] * n

#         def calculate_dp(i):
#             if length[i] != 0:
#                 return

#             length[i] = 1
#             count[i] = 1

#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     calculate_dp(j)
#                     if length[j] + 1 > length[i]:
#                         length[i] = length[j] + 1
#                         count[i] = 0
#                     if length[j] + 1 == length[i]:
#                         count[i] += count[j]

#         max_length = 0
#         result = 0
#         for i in range(n):
#             calculate_dp(i)
#             max_length = max(max_length, length[i])

#         for i in range(n):
#             if length[i] == max_length:
#                 result += count[i]

#         return result

class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n
        mx=0

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j]+1>dp[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    cnt[i]=cnt[j]
                elif nums[i] > nums[j] and dp[j]+1==dp[i]:
                    cnt[i]+=cnt[j]

            mx=max(mx,dp[i])

        ans=0
        for i in range(n):
            if dp[i]==mx:
                ans+=cnt[i]
        return ans
