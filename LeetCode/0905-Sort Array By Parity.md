---
title: 0905-Sort Array By Parity
updated: 2022-06-10 14:47:58Z
created: 2022-06-10 14:20:19Z
source: https://leetcode.com/problems/sort-array-by-parity/
tags:
  - easy
  - python
  - two pointers
---

905\. Sort Array By Parity

Easy

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return ***any array** that satisfies this condition*.

**Example 1:**

```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

```

**Example 2:**

```
Input: nums = [0]
Output: [0]

```

**Constraints:**

- `1 <= nums.length <= 5000`
- `0 <= nums[i] <= 5000`

**Solution:**
```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
                
            if nums[i] % 2 == 0: i += 1
            if nums[j] % 2 == 1: j -= 1
        return nums
```