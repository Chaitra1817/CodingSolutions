'''

36. Valid Sudoku
Solved
Medium
Topics
Companies

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m,n=len(board),len(board[0])
        r=[{} for i in range(9)]
        c=[{} for i in range(9)]
        box=[{} for i in range(9)]

        for i in range(m):
            for j in range(m):
                val=board[i][j]
                if val==".":
                    continue
                
                boxno=(i//3)*3+(j//3)

                if val in r[i]:
                    return False
                if val in c[j]:
                    return False
                if val in box[boxno]:
                    return False

                r[i][val]=1
                c[j][val]=1
                box[boxno][val]=1
                

        return True

            
