'''
939. Minimum Area Rectangle
Solved
Medium
Topics
Companies

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.
Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

'''
import sys
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans=sys.maxsize
        seen=set()
        for x1,y1 in points:
            for x2,y2 in points:
                if (x1,y2) in seen and (x2,y1) in seen:
                    ans=min(ans,abs((x2-x1)*(y2-y1)))
            seen.add((x1,y1))
        
        if ans==sys.maxsize:
            return 0
        return ans
        
