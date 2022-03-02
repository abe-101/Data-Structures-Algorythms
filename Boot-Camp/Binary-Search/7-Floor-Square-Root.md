---
title: 7-Floor-Square-Root
updated: 2022-03-02 16:29:22Z
created: 2022-02-22 20:12:07Z
tags:
  - binary search
  - easy
---

## Binary Search over Integer Space

**Level**: Easy

Find the square root of an integer X. For example, squareRoot(4) = 2.
If X is not a perfect square, find the integer floor of the square root.
For example,
squareRoot(5) & squareRoot(8) will return 2.
squareRoot(9) will return 3.

Questions to Clarify:
Q. Can the input be a negative number?
A. No, only positive numbers and zero.

## Solution

The brute force method would be to iterate from 0 to X until i^2 equals or exceeds X. We can improve this with binary search.
We can search over the integer space 0 to X/2 because the floors of square roots won't exceed X/2 (except if X=1).
At every step we check if mid's square is less or grater than X, and move accordingly.

**Pseudocode**:

```
low = 0, high = X/2
while low <= high
    find mid
    if mid*mid > X
        high = mid -1
    else if mid*mid < X
        if (mid+1)*(mid+1) > X
            we found the floor, return mid
        low = mid + 1
    else // equal to X
        return mid

return -1 // not found, shouldn't happen


```

**Test Cases**:
Edge Cases: 0
Base Cases: 1, 2, 3
Regular Cases: exact square root, 1 less/more than square root, etc.

Time Complexity: O(log(X))
Space Complexity: O(1)

**code:**

```
public static int floorSquareRootDemo(int x) {
    if (x == 0)
        return 0;


    if (x == 1)
        return 1;

    int low = 0, high = x/2;

    while (low <= high) {
        int mid = low + (high - low)/2;
        if (mid * mid > x ) {
            high = mid -1;
        } else if (mid * mid < x) {
            if ((mid+1) * (mid+1) > x)
                return mid;
            low = mid + 1;
        } else {
            return mid;
        }
    }

    return -1; // should not happen.
}

```