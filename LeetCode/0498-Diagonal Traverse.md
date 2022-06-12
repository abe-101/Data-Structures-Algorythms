---
title: 0498-Diagonal Traverse
updated: 2022-06-12 03:05:20Z
created: 2022-06-12 03:02:57Z
source: https://leetcode.com/problems/diagonal-traverse/
---

498\. Diagonal Traverse

Medium

Given an `m x n` matrix `mat`, return *an array of all the elements of the array in a diagonal order*.

**Example 1:**

![](../_resources/diag1-grid_00d606457d8c46eca784ed0f5bf28ede.jpg)

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

```

**Example 2:**

```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

```

**Constraints:**

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10<sup>4</sup>`
- `1 <= m * n <= 10<sup>4</sup>`
- `-10<sup>5</sup> <= mat[i][j] <= 10<sup>5</sup>`

**Solution:**

```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        N, M = len(mat), len(mat[0])
        result, intermediate  = [], []
        
        for d in range(N+M -1):
            intermediate.clear()
            row = 0 if d < M else d -M + 1
            col = d if d < M else M - 1
            
            while row < N and col > -1:
                intermediate.append(mat[row][col])
                row += 1
                col -= 1
                
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result
```

Time Complexity: O(M + N)
Space Complexity: O(min(N, M))