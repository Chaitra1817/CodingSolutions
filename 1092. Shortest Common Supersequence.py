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

