'''
2013. Detect Squares
Solved
Medium
Topics
Companies
Hint

You are given a stream of points on the X-Y plane. Design an algorithm that:

    Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
    Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

    DetectSquares() Initializes the object with an empty data structure.
    void add(int[] point) Adds a new point point = [x, y] to the data structure.
    int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

 

Example 1:

Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]
'''

class DetectSquares:

    def __init__(self):
        self.points=defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        cnt=0
        x1,y1=point

        for (x2,y2),n in self.points.items():
            x,y=abs(x1-x2),abs(y1-y2)
            if x==y and x>0:
                corner1=(x1,y2)
                corner2=(x2,y1)
                if corner1 in self.points and corner2 in self.points:
                    cnt+=n*self.points[corner1]*self.points[corner2]
        
        return cnt
        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
