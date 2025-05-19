'''
211. Design Add and Search Words Data Structure
Solved
Medium
Topics
Companies
Hint

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

'''

class Node:
    def __init__(self):
        self.links = {}
        self.flag = False
    
    def contains(self, ch):
        return ch in self.links
    
    def get(self, ch):
        return self.links[ch]
    
    def put(self, ch, node):
        self.links[ch] = node
    
    def setEnd(self):
        self.flag = True
    
    def isEnd(self):
        return self.flag

class WordDictionary:

    def __init__(self):
        self.node=Node()

    def addWord(self, word: str) -> None:
        node = self.node
        for ch in word:
            if not node.contains(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()
        

    def search(self, word: str) -> bool:
        node = self.node
        found=False
        def dfs(idx,node):
            if idx==len(word):
                return node.isEnd()
            
            c=word[idx]
            if c==".":
                for child in node.links.values():
                    if dfs(idx+1,child):
                        return True
                return False
            else:
                if not node.contains(c):
                    return False
                return dfs(idx+1,node.get(c))

        return dfs(0,node)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
