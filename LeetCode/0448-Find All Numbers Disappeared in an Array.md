---
title: '0448-Find All Numbers Disappeared in an Array '
updated: 2022-06-10 16:53:53Z
created: 2022-06-10 16:25:32Z
source: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
tags:
  - easy
  - in place
  - python
---

448\. Find All Numbers Disappeared in an Array

Easy

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return *an array of all the integers in the range* `[1, n]` *that do not appear in* `nums`.

**Example 1:**

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

```

**Example 2:**

```
Input: nums = [1,1]
Output: [2]

```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 10<sup>5</sup>`
- `1 <= nums[i] <= n`

**Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            x = abs(num)-1
            nums[x] = -1 * abs(nums[x])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result
```

Time Complexity: O(n)
Space Complexity: O(1)