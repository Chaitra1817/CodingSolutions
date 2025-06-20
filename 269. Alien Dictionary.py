'''
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are

by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:

Input: words = ["z","x"]
Output: "zx"

Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of only lowercase English letters.

'''

from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        d = defaultdict(int)
        connected = defaultdict(set)

        for word in words:
            for c in word:
                d[c] = 0

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            l = min(len(word1), len(word2))
            if word1[:l] == word2[:l] and len(word1) > len(word2):
                return ""
            for j in range(l):
                if word1[j] != word2[j]:
                    if word2[j] not in connected[word1[j]]:
                        connected[word1[j]].add(word2[j])
                        d[word2[j]] += 1
                    break  

        q = deque([char for char in d if d[char] == 0])
        ans = ""

        while q:
            node = q.popleft()
            ans += node
            for neigh in connected[node]:
                d[neigh] -= 1
                if d[neigh] == 0:
                    q.append(neigh)

        return ans if len(ans) == len(d) else ""
