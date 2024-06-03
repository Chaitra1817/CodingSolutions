'''
3168. Minimum Number of Chairs in a Waiting Room
Solved
Easy
Hint

You are given a string s. Simulate events at each second i:

    If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
    If s[i] == 'L', a person leaves the waiting room, freeing up a chair.

Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.

 

Example 1:

Input: s = "EEEEEEE"

Output: 7

Explanation:

After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.

Example 2:

Input: s = "ELELEEL"

Output: 2

Explanation:

Let's consider that there are 2 chairs in the waiting room. The table below shows the state of the waiting room at each second.

'''

class Solution:
    def minimumChairs(self, s: str) -> int:
        e,l=0,0
        for i in s:
            if i=="E":
                if l>0:
                    l-=1
                else:
                    e+=1
            else:
                l+=1
        return e
