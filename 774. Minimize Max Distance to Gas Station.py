'''
ou are given an integer array stations that represents the positions of the gas stations on the x-axis. You are also given an integer k.

You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new stations.

Return the smallest possible value of penalty(). Answers within 10-6 of the actual answer will be accepted.

 

Example 1:

Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.50000

Example 2:

Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
Output: 14.00000

 

Constraints:

    10 <= stations.length <= 2000
    0 <= stations[i] <= 108
    stations is sorted in a strictly increasing order.
    1 <= k <= 106

'''

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n=len(stations)

        def find(d):
            cnt=0
            prev=stations[0]
            for i in stations[1:]:
                if i-prev<=d:
                    prev=i
                else:
                    gap=i-prev
                    cnt+=math.ceil(gap/d)-1
                    prev=i
            return cnt<=k


        low=0
        high=stations[-1]-stations[0]
        ans=0
        while (high-low)>1e-6:
            mid=(low+high)/2.0
            if find(mid):
                high=mid
                ans=mid
            else:
                low=mid
        return ans

        
