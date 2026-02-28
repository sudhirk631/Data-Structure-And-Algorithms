# -*- coding: utf-8 -*-
'''
The Fibonacci series is a sequence where a term is the sum of previous two terms. 
The first two terms of the Fibonacci sequence are 0 followed by 1. 
The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21.
f(0) = 0
f(2) = 1
f(3) = 2 (f(2) + f(1))
f(4) = 3 (f(2) + f(1))
f(5) = 5
f(6) = 8
f(7) = 13
f(8) = 21

In this approach, we are optimizing the recursive approach by storing the solutions 
of already solved subproblems in a memoization table. 
This prevents recalculating the same results multiple times, 
this will reduce the exponential time complexity into a more efficient time complexity.
'''


def nthFibonacciUtil(n, dp):
    
    # Base case
    if n <= 1:
        return n

    # Check if the result is
    # already in the dp table
    if dp[n] != -1:
        return dp[n]

    # calculate Fibonacci number
    # and store it in dp table
    dp[n] = nthFibonacciUtil(n - 1, dp) + nthFibonacciUtil(n - 2, dp)

    return dp[n]


def nthFibonacci(n):

    # Create a dp table and 
    # initialize with -1(invalid value)
    dp = [-1] * (n + 1)
    
    return nthFibonacciUtil(n, dp)

n = 200
result = nthFibonacci(n)
print(result)
