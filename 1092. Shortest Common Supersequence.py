'''
1092. Shortest Common Supersequence
Hard
Topics
Companies
Hint

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of lowercase English letters.


'''

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        memo = {}

        def find(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == n:
                return str2[j:]
            if j == m:
                return str1[i:]

            if str1[i] == str2[j]:
                result = str1[i] + find(i + 1, j + 1)
            else:
                first = str1[i] + find(i + 1, j)
                second = str2[j] + find(i, j + 1)
                if len(first) < len(second):
                    result = first
                else:
                    result = second

            memo[(i, j)] = result
            return result

        return find(0, 0)


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        # Initialize the dp array with (m+1) x (n+1) dimensions for LCS calculation
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # Fill the dp array with LCS length values
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:  # If characters match
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Build the shortest common supersequence using the dp table
        i, j = m, n
        ans = ""
        
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # If characters match, add once
                ans = str1[i - 1] + ans
                i -= 1
                j -= 1
            elif dp[i][j - 1] > dp[i - 1][j]:  # If move came from left, pick from str2
                ans = str2[j - 1] + ans
                j -= 1
            else:  # If move came from top, pick from str1
                ans = str1[i - 1] + ans
                i -= 1

        # Add any remaining characters from either string
        while i > 0:
            ans = str1[i - 1] + ans
            i -= 1
        while j > 0:
            ans = str2[j - 1] + ans
            j -= 1

        return ans

