'''

(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

    MountainArray.get(k) returns the element of the array at index k (0-indexed).
    MountainArray.length() returns the length of the array.

Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

'''

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        
        def findPeak():
            l, r = 0, n-1
            while l < r:
                mid = (l + r) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def asc(l,r):
            ans=-1
            while l<=r:
                mid=(l+r)//2
                val=mountainArr.get(mid)
                if val==target:
                    ans=mid
                    r=mid-1
                elif target<val:
                    r=mid-1
                else:
                    l=mid+1
            return ans
        
        def dsc(l,r):
            ans=-1
            while l<=r:
                mid=(l+r)//2
                val=mountainArr.get(mid)
                if val==target:
                    ans=mid
                    r=mid-1
                elif val<target:
                    r=mid-1
                else:
                    l=mid+1
            return ans
            

        p=findPeak()
        l,r=0,p
        ans=asc(l,r)
        if ans==-1:
            l,r=p+1,n-1
            ans=dsc(l,r)
        return ans
