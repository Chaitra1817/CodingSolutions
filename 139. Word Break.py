'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

'''

class Node:
    def __init__(self):
        self.link = {}
        self.flag = False

    def contains(self, c):
        return c in self.link

    def get(self, c):
        return self.link.get(c)

    def put(self, c, node):
        self.link[c] = node

    def setEnd(self):
        self.flag = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Node()
        for word in wordDict:
            node = root
            for c in word:
                if not node.contains(c):
                    node.put(c, Node())
                node = node.get(c)
            node.setEnd()

        memo = {}
        n = len(s)

        def dfs(index):
            if index == n:
                return True
            if index in memo:
                return memo[index]

            node = root
            for i in range(index, n):
                c = s[i]
                if not node.contains(c):
                    break
                node = node.get(c)
                if node.flag and dfs(i + 1):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return dfs(0)
