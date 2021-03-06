'''
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

'''

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles<numExchange:
            return numBottles
        elif numBottles==numExchange:
            return numBottles+1
        else:
            ans=0
            count=numBottles
            while numBottles>= numExchange:
                cal=numBottles//numExchange
                ans+=cal
                rem=numBottles%numExchange
                numBottles=cal+rem
            
        return ans+count
        

 