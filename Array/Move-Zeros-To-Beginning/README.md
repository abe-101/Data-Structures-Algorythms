## Problem: Move Zeros to Beginning

**Level**: Easy

You are given an array of integers. Rearrange the array so that all zeroes are at
the beginning of the array.
For example,
a = [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]

## Solution:
We keep one variable to track the boundary. The boundary represents the partition between zero and
non-zero elements. We loop through the array's elements. For every zero we encounter, we move it
into the boundary and expand the boundary by 1. At the end, all elements in the boundary will be
zeroes.

  
**Pseudocode**: 
```
boundry = 0
for i in a
    if a[i] is 0
        swap a[i] with boundy
        increase boundy by 1
```

Time Complexity: O(n)  
Space Complexity: O(1)

