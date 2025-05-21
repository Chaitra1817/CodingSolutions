'''

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

'''

class Node:
    def __init__(self):
        self.links={}
        self.flag=False

    def contains(self,c):
        return c in self.links
    
    def get(self,c):
        return self.links[c]
    
    def put(self,c,node):
        self.links[c]=node

    def setEnd(self):
        self.flag=True
 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        node=Node()
        for word in words:
            root=node
            for c in word:
                if not root.contains(c):
                    root.put(c,Node())
                root=root.get(c)
            root.setEnd()
        
        visited=set()
        ans=[]
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(i,j,node,word):
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited:
                return 
            
            if not node.contains(board[i][j]):
                return
            

            visited.add((i,j))
            node=node.get(board[i][j])
            word+=board[i][j]
            
            for dr,dc in directions:
                nr,nc=i+dr,j+dc
                dfs(nr,nc,node,word)

            if node.flag and word not in ans:
                ans.append(word)

            visited.remove((i,j))

        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(i,j,node,"")

        return ans

