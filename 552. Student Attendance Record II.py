'''
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

    'A': Absent.
    'L': Late.
    'P': Present.

Any student is eligible for an attendance award if they meet both of the following criteria:

    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.

Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

Example 2:

Input: n = 1
Output: 3

Example 3:

Input: n = 10101
Output: 183236316

 

Constraints:

    1 <= n <= 105

'''


class Solution:
    def checkRecord(self, n: int) -> int:
        memo=[[[-1]*3 for _ in range(2)] for _ in range(n+1)]
        MOD=10**9+7
        def find(n,abscnt,latecnt):
            if abscnt>=2 or latecnt>=3:
                return 0
            
            if n==0:
                return 1
            
            if memo[n][abscnt][latecnt] !=-1:
                return memo[n][abscnt][latecnt]
            
            cnt=0
            # present
            cnt+=find(n-1,abscnt,0)%MOD
            #absent
            cnt+=find(n-1,abscnt+1,0)%MOD
            #late
            cnt+=find(n-1,abscnt,latecnt+1)%MOD

            memo[n][abscnt][latecnt]=cnt%MOD
            return memo[n][abscnt][latecnt]

        return find(n,0,0)


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for a in range(2):         
                for l in range(3):     
                    val = dp[i - 1][a][l]
                    if val == 0:
                        continue
                    # Add 'P': resets 'L'
                    dp[i][a][0] = (dp[i][a][0] + val) % MOD
                    # Add 'A': if not used already
                    if a < 1:
                        dp[i][a + 1][0] = (dp[i][a + 1][0] + val) % MOD
                    # Add 'L': only if < 2 lates
                    if l < 2:
                        dp[i][a][l + 1] = (dp[i][a][l + 1] + val) % MOD

        return sum(dp[n][a][l] for a in range(2) for l in range(3)) % MOD
