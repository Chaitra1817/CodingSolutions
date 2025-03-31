'''

3494. Find the Minimum Amount of Time to Brew Potions
Solved
Medium
Topics
Companies
Hint

You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.

 

Example 1:

Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:
Potion Number	Start time	Wizard 0 done by	Wizard 1 done by	Wizard 2 done by	Wizard 3 done by
0	0	5	30	40	60
1	52	53	58	60	64
2	54	58	78	86	102
3	86	88	98	102	110

As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.


'''

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        available = [0] * n  

        for j in range(m): 
            time_needed = [skill[i] * mana[j] for i in range(n)]
            cumulative_delay = 0
            min_start = 0

            for i in range(n):
                min_start = max(min_start, available[i] - cumulative_delay)
                cumulative_delay += time_needed[i]

            current_time = min_start
            for i in range(n):
                available[i] = current_time + time_needed[i]
                current_time = available[i]

        return available[-1]
