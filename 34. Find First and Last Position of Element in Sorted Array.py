'''

34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
Companies

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]



'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # ans=[]

        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         ans.append(i)
        #         break
        
        # for j in range(len(nums)-1,-1,-1):
        #     if nums[j]==target:
        #         ans.append(j)
        #         break
        
        # if len(ans)>1:
        #     return ans
        
        # return [-1,-1]
        
        # Approach 2


        def first(a,x):
            n=len(a)
            low,high=0,n-1
            first=-1
            while low<=high:
                mid=(low+high)//2
                if a[mid]==x:
                    high=mid-1
                    first=mid
                elif a[mid]>x:
                    high=mid-1
                else:
                    low=mid+1
            return first
        
        def last(a,x):
            n=len(a)
            low,high=0,n-1
            last=-1
            while low<=high:
                mid=(low+high)//2
                if a[mid]==x:
                    low=mid+1
                    last=mid
                elif a[mid]>x:
                    high=mid-1
                else:
                    low=mid+1
            return last
                    

        f=first(nums,target)
        l=last(nums,target)
        if f==-1:
            return[-1,-1]
        return[f,l]
