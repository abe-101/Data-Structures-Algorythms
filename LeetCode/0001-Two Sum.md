---
title: 0001-Two Sum
updated: 2022-07-08 21:28:26Z
created: 2022-07-08 21:26:43Z
source: https://leetcode.com/problems/two-sum/
tags:
  - arrays and hashing
  - blind 75
  - easy
  - python
---

1\. Two Sum

Easy

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]

```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]

```

**Constraints:**

- `2 <= nums.length <= 10<sup>4</sup>`
- `-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>`
- `-10<sup>9</sup> <= target <= 10<sup>9</sup>`
- **Only one valid answer exists.**

**Solution:**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
```