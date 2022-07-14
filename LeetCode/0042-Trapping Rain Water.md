---
title: 0042-Trapping Rain Water
updated: 2022-07-14 11:20:47Z
created: 2022-07-14 11:20:12Z
source: https://leetcode.com/problems/trapping-rain-water/
tags:
  - blind 75
  - hard
  - python
  - two pointers
---

42\. Trapping Rain Water

Hard

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

![](../_resources/rainwatertrap_0a731401966e44d0b54eb397c53dd228.png)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9

```

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 10<sup>4</sup>`
- `0 <= height[i] <= 10<sup>5</sup>`

**Solution:**
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) -1
        left_max, right_max = height[l], height[r]
        res = 0
        
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
                
        return res
```
Time Complexity: O(n)
Space Complexity: O(1)