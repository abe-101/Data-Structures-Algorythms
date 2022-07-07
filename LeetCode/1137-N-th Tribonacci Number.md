---
title: 1137-N-th Tribonacci Number
updated: 2022-07-06 17:00:20Z
created: 2022-07-06 16:59:36Z
source: https://leetcode.com/problems/n-th-tribonacci-number/
tags:
  - dp
  - easy
  - memoization
  - python
---

1137\. N-th Tribonacci Number

Easy

The Tribonacci sequence T<sub>n</sub> is defined as follows:

T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> \+ T<sub>n+1</sub> \+ T<sub>n+2</sub> for n >= 0.

Given `n`, return the value of T<sub>n</sub>.

**Example 1:**

```
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

```

**Example 2:**

```
Input: n = 25
Output: 1389537

```

**Constraints:**

- `0 <= n <= 37`
- The answer is guaranteed to fit within a 32-bit integer, ie. `answer <= 2^31 - 1`.

**Solution:**

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        def _tribonacci(n, memo):
            if n == 0 or n == 1:
                return n
            if n == 2:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = _tribonacci(n-1, memo) + _tribonacci(n-2, memo) + _tribonacci(n-3, memo)
            return memo[n]
        return _tribonacci(n, {})
```

Time Complexity: O(n)
Space Complexity: O(n)