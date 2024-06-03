'''
3170. Lexicographically Minimum String After Removing Stars
Solved
Medium

You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

    Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.

Return the
lexicographically smallest
resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

 

Constraints:

    1 <= s.length <= 105
    s consists only of lowercase English letters and '*'.
    The input is generated such that it is possible to delete all '*' characters.


'''

class Solution:
    def clearStars(self, s: str) -> str:
        heap, ans = [], []
        i, n = 0, len(s)
        while i < n:
            if s[i] == '*':
                el, index = heapq.heappop(heap)
                ans[-index] = 0
            else:
                heapq.heappush(heap, (s[i], -i))
            ans.append(s[i])
            i += 1
        s = ''
        for c in ans:
            if c and c != '*': s += c
        return s
