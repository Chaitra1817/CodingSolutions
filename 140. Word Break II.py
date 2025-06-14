'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

 

Constraints:

    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
    Input is generated in a way that the length of the answer doesn't exceed 105.

'''

class Trie:
    def __init__(self):
        self.link={}
        self.flag=False
    
    def contains(self,c):
        return c in self.link
    
    def get(self,c):
        return self.link[c]
    
    def put(self,c,Node):
        self.link[c]=Node
    
    def setEnd(self):
        self.flag=True
    
    def isEnd(self):
        return self.flag



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root=Trie()
        for word in wordDict:
            node=root
            for c in word:
                if not node.contains(c):
                    node.put(c,Trie())
                node=node.get(c)
            
            node.setEnd()
        
        ans=[]
        n=len(s)
        def find(idx,string,node):
            if idx==n:
                if node.isEnd():
                    ans.append(string)
                return

            if node.isEnd():
                find(idx,string+" ",root)
            if node.contains(s[idx]):
                find(idx+1,string+s[idx],node.get(s[idx]))
        
        find(0,"",root)
        return ans


        
