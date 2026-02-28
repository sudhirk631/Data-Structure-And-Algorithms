# Dynamic Programming Fundamentals
Dynamic Programming (DP) is a powerful technique used to solve problems by breaking them down into smaller, overlapping subproblems. 
Instead of recomputing solutions repeatedly, DP stores results and reuses them, making algorithms more efficient.

## Key Concepts
- Optimal Substructure: A problem has an optimal substructure if its solution can be constructed from solutions to subproblems.
- Overlapping Subproblems: DP is effective when the same subproblems are solved multiple times.
- Memoization vs Tabulation: 
    - Memoization: Top-down approach using recursion + caching.
    - Tabulation: Bottom-up approach using iteration + table filling.

## Classic Example: Fibonacci Numbers
The naive recursive solution for Fibonacci numbers has exponential time complexity. DP reduces it to linear time.
**Fibonacci Number Generation using Recursive Method (Naive)**
```language
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
**Fibonacci Number Generation using (Memoization) Dynamic Programming**
```language
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

**Fibonacci Number Generation using (Tabulation) Dynamic Programming**
```language
def fib_tab(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
```
## Why Dynamic Programming Matters
- Reduces exponential problems to polynomial time.
- Widely used in AI, optimization, and systems design.
- Forms the backbone of algorithms in graph theory, string matching, and resource allocation.

## Dynamic Programming Mind Map

A visual overview of the key concepts in Dynamic Programming:

![Dynamic Programming Mind Map](https://copilot.microsoft.com/th/id/BCO.86584586-1dd7-4c6d-ae59-9c4a2de6e051.png)


   
