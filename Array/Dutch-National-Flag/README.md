## Problem: Dutch National Flag

**Level**: Medium

You are given an array of integers and a pivot. Rearrange the array in the
following order:
[all elements less than pivot, elements equal to pivot, elements greater than pivot]
For example,
a = [5,2,4,4,6,4,4,3] and pivot = 4 --> result = [3,2,4,4,4,4,5,6].


**Pseudocode**:
``  
low_boundary = 0, high_boudary = a.lenght -1
i = 0
while i <= high_boundary
    if a[i] < pivot
        add a[i] to low boundary
        expand boudary by 1
        i++
    else if a[i] > pivot
        add a[i] to high boundary
        expand boundary by one
    else // equal to pivot
        i++
```

Time Complexity: O(n)  
Space Complexity: O(1)

