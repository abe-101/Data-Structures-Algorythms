---
title: 0215-Kth Largest Element in an Array
updated: 2022-07-05 19:26:35Z
created: 2022-07-05 19:17:14Z
source: https://leetcode.com/problems/kth-largest-element-in-an-array/
tags:
  - heap
  - medium
  - python
---

215\. Kth Largest Element in an Array

Medium

Given an integer array `nums` and an integer `k`, return *the* `k<sup>th</sup>` *largest element in the array*.

Note that it is the `k<sup>th</sup>` largest element in the sorted order, not the `k<sup>th</sup>` distinct element.

**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

```

**Constraints:**

- `1 <= k <= nums.length <= 10<sup>4</sup>`
- `-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>`

**Solution:**

```python
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num *(-1))
        
        for _ in range(1, k):
            heapq.heappop(heap)
            
        return -heappop(heap)
```