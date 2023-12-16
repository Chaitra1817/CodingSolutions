
from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):

    dp = [[-1 for _ in range(k + 1)] for _ in range(n)]

    def findSubset(idx, target, dp):
        nonlocal arr
        if target == 0:
            return True
        
        if idx == 0:
            return arr[0] == target
        
        if dp[idx][target] != -1:
            return dp[idx][target]
        
        take = findSubset(idx - 1, target, dp)
        notTake = False
        if arr[idx] <= target:
            notTake = findSubset(idx - 1, target - arr[idx], dp)

        if take or notTake:
            dp[idx][target] = True
        else:
            dp[idx][target] = False
            
        return dp[idx][target]

    return findSubset(n - 1, k, dp)
