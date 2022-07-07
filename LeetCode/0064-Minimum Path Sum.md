---
title: 0064-Minimum Path Sum
updated: 2022-07-07 00:17:38Z
created: 2022-07-07 00:16:13Z
source: https://leetcode.com/problems/minimum-path-sum/
tags:
  - dp
  - medium
  - memoization
  - python
---

64\. Minimum Path Sum

Medium

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example 1:**

![](../_resources/minpath_a849a58a4ae34751b30760b8c2df5591.jpg)

```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

```

**Example 2:**

```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

```

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 100`

**Solution:**
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def helper(r, c):
            pos = (r, c)
            if pos in memo:
                return memo[pos]
            if r == len(grid) or c == len(grid[0]):
                return float('inf')
            if r == len(grid) -1 and c == len(grid[0]) -1:
                return grid[r][c]
            down = helper(r + 1, c)
            right = helper(r, c + 1)
            memo[pos] = grid[r][c] + min(down, right)
            return memo[pos]
        
        return helper(0, 0)
```
Time Complexity: O(r**c)
Space Complexity: O(r**c)