'''
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendar class:

    MyCalendar() Initializes the calendar object.
    boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

 

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

 

Constraints:

    0 <= start < end <= 109
    At most 1000 calls will be made to book.


'''

'''
 MyCalendar:

    def __init__(self):
        self.slots = []

    def find(self, slots, start, end):
        slots.sort()
        low = 0
        high = len(slots) - 1

        while low <= high:
            mid = (low + high) // 2
            s, e = slots[mid]

            if not (end <= s or start >= e):  
                return False
            elif end <= s:
                high = mid - 1
            else:
                low = mid + 1

        return True

    def book(self, startTime: int, endTime: int) -> bool:
        if self.find(self.slots, startTime, endTime):
            self.slots.append([startTime, endTime])
            return True
        return False
'''

import bisect

class MyCalendar:

    def __init__(self):
        self.slots = [] 

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_right(self.slots, (start, end))

        if index > 0 and self.slots[index - 1][1] > start:
            return False

        if index < len(self.slots) and self.slots[index][0] < end:
            return False

        self.slots.insert(index, (start, end))
        return True
