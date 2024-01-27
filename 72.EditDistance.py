'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        i,j=len(word1),len(word2)

        @cache
        def f(i,j):
            nonlocal word1,word2
            if i<0:
                return j+1
            if j<0:
                return i+1
            
            if word1[i]==word2[j]:
                return f(i-1,j-1)
            
            return 1+min(f(i-1,j),f(i,j-1),f(i-1,j-1))
        
        return f(i-1,j-1)
        
