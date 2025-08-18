'''
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

 

Constraints:

    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] consists only of digits '0' and '1'.
    1 <= m, n <= 100

'''

'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l=len(strs)
        memo={}
        def find(idx,cnt,mcnt,ncnt):
            if idx<0:
                return cnt
            
            if mcnt==m and ncnt==n:
                return cnt
            
            if (idx,cnt,mcnt,ncnt) in memo:
                return memo[(idx,cnt,mcnt,ncnt)]
            
            take=0
            mlocal,nlocal=0,0
            for i in strs[idx]:
                if i=="0":
                    mlocal+=1
                else:
                    nlocal+=1
            
            if mlocal+mcnt<=m and nlocal+ncnt<=n:
                take=find(idx-1,cnt+1,mcnt+mlocal,ncnt+nlocal)
            notTake=find(idx-1,cnt,mcnt,ncnt)

            memo[(idx,cnt,mcnt,ncnt)] = max(take,notTake)
            return  memo[(idx,cnt,mcnt,ncnt)]

        return find(l-1,0,0,0)

 '''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:  
        l = len(strs)
        dp=[[[0]*(n+1) for _ in range(m+1)] for i in range(l+1)]     

        for i,s in enumerate(strs,1):
            z=s.count('0')
            o=len(s)-z

            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k]=dp[i-1][j][k]

                    if j>=z and k>=o:
                        dp[i][j][k]=max(dp[i][j][k],1+dp[i-1][j-z][k-o])

        
        return dp[l][m][n]
