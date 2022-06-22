---
title: 0118-Pascal's Triangle
updated: 2022-06-14 14:54:54Z
created: 2022-06-13 15:52:17Z
source: https://leetcode.com/problems/pascals-triangle/
tags:
  - easy
  - python
---

118\. Pascal's Triangle

Easy

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](../_resources/PascalTriangleAnimated2_c8c7327d02bc408ebdfdd7fdc4.gif)

**Example 1:**

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

```

**Example 2:**

```
Input: numRows = 1
Output: [[1]]

```

**Constraints:**

- `1 <= numRows <= 30`

**Solution:**

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                row = [1]
            elif i == 1:
                row = [1,1]
            else:
                row = [1]
                for j in range(1, i):
                    row.append(result[i-1][j-1] + result[i-1][j])
                row.append(1)
            result.append(row)

        return result
```