'''
You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 

Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Examples :

Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)

Input: start[] = [10, 12, 20], end[] = [20, 25, 30]
Output: 1
Explanation: Only one meetings can be held with given start and end timings.

Input: start[] = [1, 2], end[] = [100, 99]
Output: 1

'''

#User function Template for python3
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        arr=[]
        n=len(start)
        
        for i in range(n):
            arr.append([end[i],start[i]])
        
        arr.sort(key= lambda x: x[0])
        
        ans=0
        prev=float('-inf')
        for i in range(n):
            if arr[i][1]>prev:
                ans+=1
                prev=arr[i][0]
            
        return ans
        
        
        
