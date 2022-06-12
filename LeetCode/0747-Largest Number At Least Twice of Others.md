---
title: 0747-Largest Number At Least Twice of Others
updated: 2022-06-10 21:50:04Z
created: 2022-06-10 21:49:16Z
source: https://leetcode.com/problems/largest-number-at-least-twice-of-others/
tags:
  - easy
  - python
---

747\. Largest Number At Least Twice of Others

Easy

You are given an integer array `nums` where the largest integer is **unique**.

Determine whether the largest element in the array is **at least twice** as much as every other number in the array. If it is, return *the **index** of the largest element, or return* `-1` *otherwise*.

**Example 1:**

```
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

```

**Example 2:**

```
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
```

**Example 3:**

```
Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.

```

**Constraints:**

- `1 <= nums.length <= 50`
- `0 <= nums[i] <= 100`
- The largest element in `nums` is unique.

**Solution:**
```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_index = 0
        for i in range(len(nums)):
            if nums[i] > nums[largest_index]:
                largest_index = i
                
        for i in range(len(nums)):
            if i == largest_index:
                continue
            if nums[i] * 2 > nums[largest_index]:
                return -1
        return largest_index
```

Time Complexity: O(n)
Space Complexity: O(1)