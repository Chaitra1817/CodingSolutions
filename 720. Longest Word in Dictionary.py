'''
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

 

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length <= 30
    words[i] consists of lowercase English letters.

'''


class Node:
    def __init__(self):
        self.flag=False
        self.link={}
    
    def contains(self,c):
        return c in self.link
    
    def get(self,c):
        return self.link[c]
    
    def put(self,c,node):
        self.link[c]=node
    
    def setEnd(self):
        self.flag=True
    
    def isEnd(self):
        return self.flag


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root=Node()
        for word in words:
            node=root
            for c in word:
                if not node.contains(c):
                    node.put(c,Node())
                node=node.get(c)
            node.setEnd()
        
        def find(node,s):
            ans=s if node.isEnd() else ""
            for i in range(26):
                c=chr(97+i)
                if node.contains(c):
                    child=node.get(c)
                    if child.isEnd():
                        temp=find(child,s+c)
                        if len(temp)>len(ans):
                            ans=temp
                
            return ans
                
        return find(root,"")
 
