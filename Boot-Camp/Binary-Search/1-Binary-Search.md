---
title: 1-Binary-Search
updated: 2022-03-02 15:51:17Z
created: 2022-02-28 16:42:46Z
latitude: 40.71230000
longitude: -74.00680000
altitude: 0.0000
tags:
  - binary search
---

## Binary Search

Given a sorted array, search for a target item?

**Level**: Easy

Questions to Clarify:  
Q. How do you want the output?  
A. Return the index of the target item.

Q. What do do if target was not found?  
A. Return -1

## Solution

Time Complexity: O(log(n))
Remember, log(n) here is base 2, because we are dividing the work by 2 each time.
Space Complexity: O(1)

**code:**

```java
public static int search(int[] a, int target) {
    if (a == null || target == null)
        return -1;
    
    int low = 0, high = a.legnth - 1;

    while (low <= high) {
        int mid = low + (high - low)/2;
        if (a[mid] < target) {
            low = mid + 1;
        } else if (a[mid] > target) {
            high = mid -1;
        } else {
            return mid;
        }
    }

    return -1;
}
```