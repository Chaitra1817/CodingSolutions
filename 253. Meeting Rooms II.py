'''
253. Meeting Rooms II
Solved
Medium
Topics
Companies
Hint

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap_room=[]
        intervals.sort(key=lambda x:x[0])

        heapq.heappush(heap_room,intervals[0][1])

        for i in intervals[1:]:
            if heap_room[0]<=i[0]:
                heapq.heappop(heap_room)
            
            heapq.heappush(heap_room,i[1])

        return len(heap_room)
