---
title: 0977- Squares of a Sorted Array
updated: 2022-06-10 16:54:10Z
created: 2022-06-10 16:52:46Z
source: https://leetcode.com/problems/squares-of-a-sorted-array/
tags:
  - easy
  - python
  - two pointers
---

977\. Squares of a Sorted Array

Easy

Given an integer array `nums` sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

```

**Example 2:**

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

```

**Constraints:**

- `1 <= nums.length <= 10<sup>4</sup>`
- `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`
- `nums` is sorted in **non-decreasing** order.

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

**Soolution:**

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        
        start, end = 0, len(nums)-1
        result = [None]*len(nums)
        resultIndex = len(nums)-1
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                result[resultIndex] = nums[start] ** 2
                resultIndex -= 1
                start += 1
            else:
                result[resultIndex] = nums[end] ** 2
                resultIndex -= 1
                end -= 1
        return result
```

Time Complexity: O(n)
Space Complexity: O(1)