---
title: 0912-Sort an Array
updated: 2022-07-13 12:21:42Z
created: 2022-07-13 12:20:49Z
source: https://leetcode.com/problems/sort-an-array/
---

912\. Sort an Array

Medium

Given an array of integers `nums`, sort the array in ascending order.

**Example 1:**

```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

```

**Example 2:**

```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

```

**Constraints:**

- `1 <= nums.length <= 5 * 10<sup>4</sup>`
- `-5 * 10<sup>4</sup> <= nums[i] <= 5 * 10<sup>4</sup>`

**Solution:**
```python
from collections import deque

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(list_1, list_2):
            list_1 = deque(list_1)
            list_2 = deque(list_2)
            merged = []


            while list_1 and list_2:
                if list_1[0] < list_2[0]:
                    merged.append(list_1.popleft())
                else:
                    merged.append(list_2.popleft())
            merged += list_1
            merged += list_2
            return merged
        
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_sorted = self.sortArray(nums[:mid])
        right_sorted = self.sortArray(nums[mid:])
        return merge(left_sorted, right_sorted)
```
Time Complexity: O(n log n)
Space Complexity: O(n)