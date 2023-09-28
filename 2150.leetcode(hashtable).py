"""
You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.

 

Example 1:

Input: nums = [10,6,5,8]
Output: [10,8]
Explanation: 
- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.

"""

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        # TLL
        # ans = []
        # for i in range(len(nums)):
        #     temp = nums[:i] + nums[i+1:]
        #     if (nums[i] + 1) not in temp and (nums[i] - 1) not in temp and nums[i] not in temp:
        #         ans.append(nums[i])
        # return ans

        dic={}
        ans=[]
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for i in nums:
            if dic[i]==1:
                if (i-1 not in dic) and (i+1 not in dic):
                    ans.append(i)
        return ans
  

