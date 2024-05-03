'''
252. Meeting Rooms
Solved
Easy
Topics
Companies

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true


'''

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # First, sort the intervals based on their start times.
        intervals.sort(key=lambda x: x[0])

        # Now, go through the sorted intervals and check for any overlaps.
        for i in range(1, len(intervals)):
            # If the start of the current interval is less than the end of the previous, they overlap.
            if intervals[i][0] < intervals[i-1][1]:
                return False

        # If no overlaps are found, return True.
        return True
