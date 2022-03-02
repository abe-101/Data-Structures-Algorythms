---
title: 5-Cyclically-Sorted-Arrays
updated: 2022-03-02 15:30:45Z
created: 2022-03-01 19:16:13Z
tags:
  - binary search
  - easy
---

## Cyclically Sorted Arrays

**Level**: Easy

Given an array that is cyclically sorted, find the minimum element. A cyclically sorted array is a sorted array rotated by some number of elements. Assume all elements are unique.
For example:
A = \[4,5,1,2,3\], which is just \[1,2,3,4,5\] rotated by 2
Result = index 2

Questions to Clarify:
Q. How do you want the input
A. Return the index of the min item.

Q.Can the array be rotated by 0 elements? i.e, a normal sorted array?
A. Yes

## Solution

Using binary search. The last element k will tell us if an element is part of first group or last group. (group 1 being element that have been rotated).
Now we can test any item in ith element and check which group its in, and know which direction to go:
for any a\[i\] we encounter:
if a\[i\] <= lastElement, it is in group 1. we go left.
if a\[i\] > lastElement, it is in group 2. we go right.

We know we reached min if the element before it is greater. or in the case when there is no rotation there will be nothing on the left.
Now we have 3 essential conditions for binary search.

**Pseudocode**:

```
right = a[a.length - 1] // last element
while start <= end
    find mid
    if mid <= right and left is greater or no left
        return mid
    if mid > right
        go right, start = mid + 1
    else
        go left, end = mid - 2
```

**Test Cases**:
Edge Cases: empty array, null array
Base Cases: one element, two elements (rotated by 0 & 1)
Regular Cases: rotated, not rotated

Time Complexity: O(log(n))
Space Complexity: O(1)

**code:**

```
public static int cyclicallySortedMin(int[] a) {
    if (a == null) {
        return -1;
    }

    int low = 0, high = a.length -1, right = a[a.length -1];
    int results = -1;
    while (low <= high) {
        int mid = low + ((high - low) >> 1);
        if (a[mid] <= right && (mid == 0 || a[mid - 1] > a[mid])) {
            return mid;
        } else if (a[mid] > right) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return -1;
}
```