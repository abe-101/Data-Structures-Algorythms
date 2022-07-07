---
title: 0063-Unique Paths II
updated: 2022-07-07 00:16:38Z
created: 2022-07-06 21:07:39Z
source: https://leetcode.com/problems/unique-paths-ii/
tags:
  - dp
  - medium
  - memoization
  - python
---

63\. Unique Paths II

Medium

You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m-1][n-1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The testcases are generated so that the answer will be less than or equal to `2 * 10<sup>9</sup>`.

**Example 1:**

![](../_resources/robot1_72f2e5edbce0466ca10d2d912515dec7.jpg)

```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

```

**Example 2:**

![](../_resources/robot2_136db41c2b4e4ec8aa99560cfaf5c07b.jpg)

```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

```

**Constraints:**

- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`.

**Solution:**

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def _uniquePathsWithObstacles(grid, r, c, memo):
            pos = (r, c)
            if pos in memo:
                return memo[pos]
            if r == len(grid) or c == len(grid[0]) or grid[r][c] == 1:
                return 0
            if r == len(grid) -1 and c == len(grid[0]) -1:
                return 1
            down = _uniquePathsWithObstacles(obstacleGrid, r + 1, c, memo)
            right = _uniquePathsWithObstacles(obstacleGrid, r, c + 1, memo)
            memo[pos] = down + right
            return memo[pos]
        
        return _uniquePathsWithObstacles(obstacleGrid, 0, 0, {})
```

Time Complexity: O(r**c)
Space Complexity: O(r**c)