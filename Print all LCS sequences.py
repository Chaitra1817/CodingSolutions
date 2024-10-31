'''

You are given two strings s and t. Now your task is to print all longest common sub-sequences in lexicographical order.

Note -  A Sub-sequence is derived from another string by deleting some or none of the elements without changing the order of the remaining elements.

Example 1:

Input: s = abaaa, t = baabaca
Output: aaaa abaa baaa
Explanation - Length of lcs is 4, in lexicographical order they are aaaa, abaa, baaa

Example 2:

Input: s = aaa, t = a
Output: a

Your Task:
You do not need to read or print anything. Your task is to complete the function all_longest_common_subsequences() which takes strings s and t as first and second parameters respectively and returns a list of strings which contains all possible longest common subsequences in lexicographical order.
 

Expected Time Complexity: O(n3)
Expected Space Complexity: O(k * n) where k is a constant less than n.

'''

class Solution:
    def all_longest_common_subsequences(self, s, t):
        n = len(s)
        m = len(t)
        
        # Initialize dp array with size (n+1) x (m+1) with all values set to 0
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        # Fill the dp array
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Memoized backtracking to find all unique LCS strings
        memo = {}
        
        def backtrack(i, j):
            # Base case: if we reach the start of either string, return a set with an empty string
            if i == 0 or j == 0:
                return {""}
            
            # If already computed, return the cached result
            if (i, j) in memo:
                return memo[(i, j)]
            
            lcs_set = set()
            # If characters match, add them to all LCS strings formed from previous diagonal
            if s[i-1] == t[j-1]:
                for seq in backtrack(i-1, j-1):
                    lcs_set.add(seq + s[i-1])
            else:
                # If characters do not match, take the LCS from the larger value (up or left)
                if dp[i-1][j] == dp[i][j]:
                    lcs_set.update(backtrack(i-1, j))
                if dp[i][j-1] == dp[i][j]:
                    lcs_set.update(backtrack(i, j-1))
            
            # Memoize result for current (i, j)
            memo[(i, j)] = lcs_set
            return lcs_set

        # Get all unique LCS strings from the backtrack function starting at the end of dp table
        all_lcs = sorted(backtrack(n, m))
        
        return all_lcs
