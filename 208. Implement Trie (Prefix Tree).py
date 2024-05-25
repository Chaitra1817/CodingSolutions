'''
208. Implement Trie (Prefix Tree)
Solved
Medium
Topics
Companies

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

'''

class Node:
    def __init__(self):
        self.links=[None]*26
        self.flag=False
    
    def contains(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    
    def put(self,ch,node):
        self.links[ord(ch)-ord('a')]=node
    
    def setEnd(self):
        self.flag=True
    
    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        self.root=Node()
        
    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            if not node.contains(ch):
                node.put(ch,Node())
            node=node.get(ch)
        node.setEnd()

    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if not node.contains(ch):
                return False
            node=node.get(ch)
        
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            if not node.contains(ch):
                return False
            node=node.get(ch)
        return True  
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
