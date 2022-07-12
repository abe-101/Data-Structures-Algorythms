---
title: 0217-Contains Duplicate
updated: 2022-07-08 21:15:42Z
created: 2022-07-08 21:14:12Z
source: https://leetcode.com/problems/contains-duplicate/
tags:
  - arrays and hashing
  - blind 75
  - easy
  - python
---

217\. Contains Duplicate

Easy

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: true

```

**Example 2:**

```
Input: nums = [1,2,3,4]
Output: false

```

**Example 3:**

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

```

**Constraints:**

- `1 <= nums.length <= 10<sup>5</sup>`
- `-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>`

**Solution:**
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```