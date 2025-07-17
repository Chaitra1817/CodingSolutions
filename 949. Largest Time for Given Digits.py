'''
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

 

Example 1:

Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

Example 2:

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.

 

Constraints:

    arr.length == 4
    0 <= arr[i] <= 9

'''

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        for h in range(23,-1,-1):
            for m in range(59,-1,-1):
                h1,h2=h//10,h%10
                m1,m2=m//10,m%10

                time=[h1,h2,m1,m2]
                if sorted(time)==arr:
                    return str(h1)+str(h2)+":"+str(m1)+str(m2)
        return ""
        
