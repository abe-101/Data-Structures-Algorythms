---
title: 0509-Fibonacci Number
updated: 2022-07-06 16:53:00Z
created: 2022-07-06 16:51:51Z
source: https://leetcode.com/problems/fibonacci-number/
tags:
  - easy
  - fibonacci
  - memoization
  - python
---

509\. Fibonacci Number

Easy

The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

```

Given `n`, calculate `F(n)`.

**Example 1:**

```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

```

**Example 2:**

```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

```

**Example 3:**

```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

```

**Constraints:**

- `0 <= n <= 30`

**Solution:**

```python
class Solution:
    def fib(self, n: int) -> int:
        def _fib(n, memo):
            if n == 0 or n == 1:
                return n
            if n in memo:
                return memo[n]
            memo[n] = _fib(n-1, memo) + _fib(n-2, memo)
            return memo[n]
        return _fib(n, {})
```

Time Complexity: O(n)
Space Complexity: O(n)