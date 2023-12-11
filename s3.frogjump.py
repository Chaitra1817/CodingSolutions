#Most optimal 

'''
from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    prev1=0
    prev2=0

    for i in range(1,n):
        first=prev1+abs(heights[i]-heights[i-1])
        second=float('inf')
        if i>1:
            second=prev2+abs(heights[i]-heights[i-2])
        cur=min(first,second)
        prev2=prev1
        prev1=cur
        

    return prev1

'''
