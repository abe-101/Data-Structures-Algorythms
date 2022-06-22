---
title: 0209-Minimum Size Subarray Sum
updated: 2022-06-14 14:22:52Z
created: 2022-06-14 14:21:41Z
source: https://leetcode.com/problems/minimum-size-subarray-sum/
tags:
  - medium
  - python
  - two pointers
---

209\. Minimum Size Subarray Sum

Medium

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a **contiguous subarray** `[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]` of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

**Example 1:**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

**Example 2:**

```
Input: target = 4, nums = [1,4,4]
Output: 1

```

**Example 3:**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```

**Constraints:**

- `1 <= target <= 10<sup>9</sup>`
- `1 <= nums.length <= 10<sup>5</sup>`
- `1 <= nums[i] <= 10<sup>5</sup>`

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

**Solution:**
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer  = float('inf')
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= target:
                answer = min(answer, i + 1 - left)
                sum -= nums[left]
                left += 1
                
        return 0 if answer == float('inf') else answer
```

Time Complexity: O(n)
Space Complexity: O(1)