'''

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

 

Constraints:

    1 <= source.length, target.length <= 1000
    source and target consist of lowercase English letters.

'''

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        m,n=len(source),len(target)

        def find(i,j,k):
            if j==n:
                return k
            elif i>=m:
                return find(0,j,k+1)
            

            for ni in range(i,m):
                if source[ni]==target[j]:
                    return find(ni+1,j+1,k)
            
            return find(0,j,k+1) if i!=0 else -1


        return find(0,0,1)
        
