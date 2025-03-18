

def subsetSumToK(n, k, arr):
    arr.sort()

    dp = [[False for _ in range(k+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0]=True
    
    for j in range(1,k+1):
        if arr[0]==j:
            dp[0][j]=True
    
    for i in range(1,n):
        for j in range(1,k+1):
            dp[i][j]=dp[i-1][j]
            if j>=arr[i]:
                dp[i][j]=dp[i][j] or dp[i-1][j-arr[i]]
                

    idx = []
    
    if not dp[n-1][k]:
        return []

    i, j = n-1, k
    while i >= 0 and j > 0:
        if i == 0 or not dp[i-1][j]: 
            idx.append(i)
            j -= arr[i]  
        i -= 1  

    res = []
    for i in idx:
        res.append(arr[i])
        
    return res



    


        
        



    

