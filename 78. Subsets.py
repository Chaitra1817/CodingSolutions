'''
78. Subsets
Solved
Medium
Topics
Companies

Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
     #powerset
        n=1<<len(nums)
        m=len(nums)
        ans=[]
        for num in range(n):
            l=[]
            for i in range(m):
                if(num & 1<<i):
                    l.append(nums[i])
            ans.append(l)
        
        return ans

# APPROACH 2 Recursion
n = len(nums)
        ans = []

        def find(idx, tmp):
            if idx == n:
                ans.append(tmp)  # Append the current subset
                return
            
            # Include the current element
            find(idx + 1, tmp + [nums[idx]])
            
            # Exclude the current element
            find(idx + 1, tmp)

        find(0, [])
        return ans

