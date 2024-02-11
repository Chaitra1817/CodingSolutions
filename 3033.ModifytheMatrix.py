'''
Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to matrix, then replace each element with the value -1 with the maximum element in its respective column.

Return the matrix answer.

 Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
Output: [[1,2,9],[4,8,6],[7,8,9]]
Explanation: The diagram above shows the elements that are changed (in blue).
- We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
- We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.

'''

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        
        for j in range(n):
            max_val = float('-inf')
            for i in range(m):
                if matrix[i][j] != -1:
                    max_val = max(max_val, matrix[i][j])
            for i in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_val
        
        return matrix
