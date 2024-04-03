'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def find(i, j, k):
            if k == len(word):
                return True  # Entire word has been found
            
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
                return False  # Out of bounds or character does not match
            
            temp = board[i][j]  # Save the character at board[i][j]
            board[i][j] = "#"  # Mark the cell as visited
            
            # Explore all possible directions
            found = (find(i, j + 1, k + 1) or find(i + 1, j, k + 1) or
                     find(i, j - 1, k + 1) or find(i - 1, j, k + 1))
            
            board[i][j] = temp  # Restore the character at board[i][j]
            return found
        
        for i in range(m):
            for j in range(n):
                if find(i, j, 0):  # Start searching from cell (i, j)
                    return True
        
        return False
