'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

'''

from collections import deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        
        s = set(wordList)
        queue = deque()
        queue.append([beginWord])
        
        res = []
        found_end = False  

        while queue and not found_end:
            size = len(queue)
            visited = set() 

            for _ in range(size):
                path = queue.popleft()
                last_word = path[-1]

                if last_word == endWord:
                    res.append(path)
                    found_end = True
                else:
                    for i in range(len(last_word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = last_word[:i] + c + last_word[i+1:]
                            if new_word in s:
                                new_path = path + [new_word]
                                queue.append(new_path)
                                visited.add(new_word)

            for w in visited:
                s.remove(w)

        return res
