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
'''

def nthFibonacci(n):
    # base case
    if n <= 1:
        return n
    
    # sum of the two preceding Fibonacci numbers
    return nthFibonacci(n - 1) + nthFibonacci(n - 2)


n = 10
result = nthFibonacci(n)
print(result)

'''
Time Complexity: O(2^n), 
because each state requires answers from previous two states, 
and thus calls the function for both of those states recursively.

Auxiliary Space: O(n), due to recursion stack
'''
