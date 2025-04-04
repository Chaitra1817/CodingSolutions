'''

You are given a string s and an integer k.

In one operation, you can replace the character at any position with the next or previous letter in the alphabet (wrapping around so that 'a' is after 'z'). For example, replacing 'a' with the next letter results in 'b', and replacing 'a' with the previous letter results in 'z'. Similarly, replacing 'z' with the next letter results in 'a', and replacing 'z' with the previous letter results in 'y'.

Return the length of the longest

of s that can be obtained after performing at most k operations.

 

Example 1:

Input: s = "abced", k = 2

Output: 3

Explanation:

    Replace s[1] with the next letter, and s becomes "acced".
    Replace s[4] with the previous letter, and s becomes "accec".

The subsequence "ccc" forms a palindrome of length 3, which is the maximum.

'''

def cost(a, b):
    diff = abs(ord(a) - ord(b))
    return min(diff, 26 - diff)

class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, j, r):
            if i > j:
                return 0
            if i == j:
                return 1

            if s[i] == s[j]:
                return 2 + dp(i+1, j-1, r)
            else:
                c = cost(s[i], s[j])
                matchVal = 0
                if c <= r:
                    matchVal = 2 + dp(i+1, j-1, r - c)

                skipVal = max(dp(i+1, j, r), dp(i, j-1, r))
                return max(matchVal, skipVal)

        return dp(0, n-1, k)

