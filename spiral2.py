'''
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Example 1:Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0 for i in range(n)]for _ in range(n)]
        left=0
        right=n-1
        top=0
        bottom=n-1
        num=1
        while(left<=right and top<=bottom):
            for i in range(left,right+1):
                matrix[top][i]=num
                num+=1
            top+=1
            for j in range(top,bottom+1):
                matrix[j][right]=num
                num+=1
            right-=1
            for i in range(right,left-1,-1):
                matrix[bottom][i]=num
                num+=1
            bottom-=1
            for j in range(bottom,top-1,-1):
                matrix[j][left]=num
                num+=1
            left+=1
        return matrix
        