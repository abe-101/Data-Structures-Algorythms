## Problem: Move Zeros to End

**Level**: Easy
Given an array of integers, rearrange the elements such that all zeros are
moved to the end of the array.

## Solution:
Keep a pointer named 'boundary' that tracks the zero-boundary at the end of the array.
Everything after this boundary contains only zeros. We loop through the array from the end
and place all zeroes into this boundary.

**Pseudocode**:
```
boundary = a.length - 1
for i is a.length-1 to 0
    if a[i] is 0
        put a[i] in the zero boundary
        expand boundary by 1
```

Time Complexity: O(n)  
Space Complexity: O(1)

