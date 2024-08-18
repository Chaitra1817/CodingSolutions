'''
3248. Snake in Matrix
Solved
Easy
Topics
Companies
Hint

There is a snake in an n x n matrix grid and can move in four possible directions. Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.

The snake starts at cell 0 and follows a sequence of commands.

You are given an integer n representing the size of the grid and an array of strings commands where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT". It's guaranteed that the snake will remain within the grid boundaries throughout its movement.

Return the position of the final cell where the snake ends up after executing commands.

 

Example 1:

Input: n = 2, commands = ["RIGHT","DOWN"]

Output: 3

Explanation:
0	1
2	3
0	1
2	3
0	1
2	3

Example 2:

Input: n = 3, commands = ["DOWN","RIGHT","UP"]

Output: 1

Explanation:
0	1	2
3	4	5
6	7	8
0	1	2
3	4	5
6	7	8
0	1	2
3	4	5
6	7	8
0	1	2
3	4	5
6	7	8

 '''
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i,j=0,0
        for k in commands:
            if k=='RIGHT':
                j+=1
            elif k=='LEFT':
                j-=1
            elif k=='DOWN':
                i+=1
            else:
                i-=1
        
        return (i*n)+j