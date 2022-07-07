---
title: '0322-Coin Change '
updated: 2022-07-06 18:47:13Z
created: 2022-07-06 18:46:07Z
source: https://leetcode.com/problems/coin-change/
tags:
  - dp
  - medium
  - memoization
  - python
---

322\. Coin Change

Medium

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return *the fewest number of coins that you need to make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1

```

**Example 3:**

```
Input: coins = [1], amount = 0
Output: 0

```

**Constraints:**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2<sup>31</sup> - 1`
- `0 <= amount <= 10<sup>4</sup>`

**Solution:**

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def _coinChange(coins, amount, memo):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            min_coins = float('inf')
            for coin in coins:
                num_coins = 1 + _coinChange(coins, amount - coin, memo)
                min_coins = min(min_coins, num_coins)
            memo[amount]= min_coins
            return min_coins
        
        ans = _coinChange(coins, amount, {})
        if ans == float('inf'):
            return -1
        else:
            return ans
```

Time Complexity: O(a*c)
Space Complexity: O(a)