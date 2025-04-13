'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


 '''

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        arr=[]
        for i in nums:
            if i%2==0:
                arr.append(0)
            else:
                arr.append(1)


        def find(target):
            if target<0:
                return 0
            l, r = 0, 0
            n = len(arr)
            total = 0
            cnt=0
            while r < n:
                total += arr[r]

                while total >target:  
                    total -= arr[l]
                    l += 1
                
                cnt+=r-l+1
                r += 1  
            
            return cnt
        return find(k)-find(k-1)
