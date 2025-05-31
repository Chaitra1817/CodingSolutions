'''

Given an integer array nums that may contain duplicates, return all possible

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10

'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        nsubsets=1<<n
        for i in range(nsubsets):
            temp=[]
            for j in range(n):
                if (i>>j) & 1:
                    temp.append(nums[j])
            if temp not in res:
                res.append(temp)

        return res
