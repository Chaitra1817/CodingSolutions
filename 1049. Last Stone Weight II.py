'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:

Input: stones = [31,26,33,21,40]
Output: 5

 

Constraints:

    1 <= stones.length <= 30
    1 <= stones[i] <= 100

'''
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2
        n=len(stones)
        memo={}

        def find(idx,cur):
            if idx<0:
                return cur
            
            if cur==target:
                return cur
            
            if (idx,cur) in memo:
                return memo[(idx,cur)]
            
            take=0
            if cur+stones[idx]<=target:
                take=find(idx-1,cur+stones[idx])
            notTake=find(idx-1,cur)

            memo[(idx,cur)] = max(take,notTake)
            return memo[(idx,cur)]
        
        closest_target=find(n-1,0)

        return total-2*closest_target

'''

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2
        n=len(stones)
        dp=[[0 for j in range(target+1)] for i in range(n+1)]


        for i in range(1,n+1):
            for j in range(target+1):
                take=0
                if stones[i - 1] <= j:
                    take=dp[i-1][j-stones[i-1]]+stones[i-1]
                notTake=dp[i-1][j]
                dp[i][j]=max(take,notTake)
        
        return total-2*dp[n][target]
