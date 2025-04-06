'''
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

    (startx, starty): The bottom-left corner of the rectangle.
    (endx, endy): The top-right corner of the rectangle.

Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

    Each of the three resulting sections formed by the cuts contains at least one rectangle.
    Every rectangle belongs to exactly one section.

Return true if such cuts can be made; otherwise, return false.

 

Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true


'''

from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        x=[(r[0],r[2]) for r in rectangles]
        y=[(c[1],c[3]) for c in rectangles]
        x.sort()
        y.sort()

        def find(axis):
            cnt=0
            prevend=-1
            for start,end in axis:
                if prevend<=start:
                    cnt+=1
                    prevend=end
                else:
                    prevend=max(prevend,end)
            return cnt


        ans=max(find(x),find(y))
        return ans>=3
        


