---
title: 0198-Rotate Array
updated: 2022-06-14 14:40:15Z
created: 2022-06-14 14:39:40Z
source: https://leetcode.com/problems/rotate-array/
tags:
  - medium
  - python
  - two pointers
---

189\. Rotate Array

Medium

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

```

**Example 2:**

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

```

**Constraints:**

- `1 <= nums.length <= 10<sup>5</sup>`
- `-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1`
- `0 <= k <= 10<sup>5</sup>`

**Follow up:**

- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

**Solution:**
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(a, start, end):
            while start < end:
                a[start], a[end] = a[end], a[start]
                start += 1
                end -= 1
                
        k = k % len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
```

Time Complexity: O(n)
Space Complexity: O(1)