'''

# Recursion
def maximumNonAdjacentSum(nums): 
    n=len(nums) 

    def findSubSequences(idx,nums):
        if idx==0:
            return nums[idx]
        
        if idx<0:
            return 0
        
        pick=nums[idx]+findSubSequences(idx-2,nums)
        notPick=findSubSequences(idx-1,nums)

        return max(pick,notPick)

    return findSubSequences(n-1,nums)  


#Memoization
def maximumNonAdjacentSum(nums): 
    n=len(nums) 
    dp=[-1]*n

    def findSubSequences(idx,nums,dp):
        if idx==0:
            return nums[idx]
        
        if idx<0:
            return 0
        
        if dp[idx]!=-1:
            return dp[idx]
        
        pick=nums[idx]+findSubSequences(idx-2,nums,dp)
        notPick=findSubSequences(idx-1,nums,dp)

        dp[idx]=max(pick,notPick)
        return dp[idx]

    return findSubSequences(n-1,nums,dp)  



  #Tabulation with space optimization

  
def maximumNonAdjacentSum(nums): 
    prev=nums[0]
    prev2=0
    for i in range(1,n):
        if i==0:
            return nums[i]
        if i<0:
            return 0
        
        take=nums[i]
        if i>1:
            take+=prev2
        notTake=prev

        cur=max(take,notTake)
        prev2=prev
        prev=cur

    return prev
