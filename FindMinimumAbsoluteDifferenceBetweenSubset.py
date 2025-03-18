

def minAbsDiff(arr, n):
    total = sum(arr)
    target = total // 2  

    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True  

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i - 1][j]  
            if j >= arr[i - 1]:  
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    for j in range(target, -1, -1):
        if dp[n][j]:
            return total - 2 * j  

    return total

# Test cases
ans = minAbsDiff([1, 6, 11, 5], 4)
print(ans)  # Output: 1

ans = minAbsDiff([1, 2, 7], 3)
print(ans)  # Output: 4
