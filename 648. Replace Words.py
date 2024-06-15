'''
648. Replace Words
Solved
Medium
Topics
Companies

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

'''

from typing import List

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False
        self.prefix_count = 0
        self.end_count = 0
    
    def contains(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    
    def setEnd(self):
        self.flag = True
    
    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.contains(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()
    
    def shortest_root(self, word):
        current = self.root
        for i in range(len(word)):
            c = word[i]
            if not current.contains(c):
                # There is not a corresponding root in the trie
                return word
            current = current.get(c)
            if current.isEnd():
                return word[: i + 1]
        # There is not a corresponding root in the trie
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_array = sentence.split()
        dict_trie = Trie()
        for word in dictionary:
            dict_trie.insert(word)
        
        for i in range(len(word_array)):
            word_array[i] = dict_trie.shortest_root(word_array[i])

        return " ".join(word_array)

        # Appoach 2

        # word_array = sentence.split()

        # def shortest_root(word):
        #     # Find the shortest root of the word in the dictionary
        #     for i in range(len(word)):
        #         root = word[0:i]
        #         if root in dictionary:
        #             return root
        #     # There is not a corresponding root in the dictionary
        #     return word

        # # Replace each word in sentence with the corresponding shortest root
        # for word in range(len(word_array)):
        #     word_array[word] = shortest_root(word_array[word])

        # return " ".join(word_array)

        

