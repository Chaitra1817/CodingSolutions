'''
1296. Divide Array in Sets of K Consecutive Numbers
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.

 

Constraints:

    1 <= k <= nums.length <= 105
    1 <= nums[i] <= 109


'''

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        d=Counter(nums)
        n=len(nums)

        if n%k!=0:
            return False

        for num in nums:
            if d[num]==0:
                continue
            
            for x in range(num,num+k):
                if d[x]==0:
                    return False
                
                d[x]-=1
        return True
    
