'''
3169. Count Days Without Meetings
Solved
Medium
Hint

You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

'''

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        # Step 1: Sort the meetings by their start day
        meetings.sort()
        
        # Step 2: Merge overlapping meetings
        merged_meetings = []
        current_start, current_end = meetings[0]
        
        for start, end in meetings[1:]:
            if start <= current_end + 1:
                current_end = max(current_end, end)
            else:
                merged_meetings.append((current_start, current_end))
                current_start, current_end = start, end
        
        # Append the last interval
        merged_meetings.append((current_start, current_end))
        
        # Step 3: Calculate the total number of days covered by meetings
        days_with_meetings = sum(end - start + 1 for start, end in merged_meetings)
                
        return days - days_with_meetings
        
