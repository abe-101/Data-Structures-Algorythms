---
title: 0011-Container With Most Water
updated: 2022-07-10 21:52:38Z
created: 2022-07-10 21:52:04Z
source: https://leetcode.com/problems/container-with-most-water/
---

11\. Container With Most Water

Medium

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i<sup>th</sup>` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

**Example 1:**

<img width="600" height="287" src="../_resources/question_11_954347195731427e80f01adf1d9b7a6f.jpg" class="jop-noMdConv">

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

**Example 2:**

```
Input: height = [1,1]
Output: 1

```

**Constraints:**

- `n == height.length`
- `2 <= n <= 10<sup>5</sup>`
- `0 <= height[i] <= 10<sup>4</sup>`

**Solution:**
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
                
        return res
```
