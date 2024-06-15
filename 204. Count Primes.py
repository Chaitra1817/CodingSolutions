'''
204. Count Primes
Solved
Medium
Topics
Companies
Hint

Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0

'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [True] * n
        primes[0], primes[1] = False, False  # 0 and 1 are not prime numbers

        for i in range(2, int(sqrt(n)) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        
        return sum(primes)
