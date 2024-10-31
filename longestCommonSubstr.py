'''
You are given two strings s1 and s2. Your task is to find the length of the longest common substring among the given strings.

'''
#User function Template for python3

class Solution:
    def longestCommonSubstr(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_len = 0  # To store the length of the longest common substring
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:  # Check characters at the correct indices
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])  # Update the maximum length found
                else:
                    dp[i][j] = 0  # Reset for non-matching characters
        
        return max_len
        
        
class Solution:
    def longestCommonSubstr(self, s1, s2):
        m, n = len(s1), len(s2)
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        max_length = 0  # Track the max length globally

        def find(i, j, l):
            nonlocal max_length
            if i >= m or j >= n:
                return l
            
            # Case when characters match
            if s1[i] == s2[j]:
                l = find(i + 1, j + 1, l + 1)
                max_length = max(max_length, l)  # Update max length found
            else:
                # Reset length if characters don’t match
                find(i, j + 1, 0)
                find(i + 1, j, 0)
                l = 0

            # No memoization here, as we’re only using `max_length`
            return l

        find(0, 0, 0)
        return max_length
