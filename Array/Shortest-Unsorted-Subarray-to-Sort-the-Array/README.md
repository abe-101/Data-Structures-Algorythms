##  Shortest Unsorted Subarray to Sort the Array


**Level**: Medium

Given an array of integers, find the shortest sub array, that if sorted, results in the
entire array being sorted.  

For example:  

[1,2,4,5,3,5,6,7] --> [4,5,3] - If you sort from indices 2 to 4, the entire array is sorted.  

[1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4] - If you sort from indices 1 to 5, the entire array is sorted.  


Questions to Clarify:
Q. How to return the results?
A. return the result as a pair indies


## Solution
We need to find the first dip from the start and the the first bump from the end. we then need to expand start if any previos numbers are greater and we need to expand end if any numbers after are less.


**Pseudocode**:
```
start = first dip (when traversing from 0)
if no dip, array is sorted return

end = first bump ( when traversing from the end to 0)

find max and min in subarray [start, end]
expand start left, until find an element less than min
expand end right, until you find element greater than max

return start, end
```
**Test Cases**:
Edge Cases: empty array, null array  
Base Case: one element, 2 elements (sorted and unsorted)  
Regular Case: array already sorted, unsorted portion at beginning/end etc.  


Time Complexity: O(n)
Space Complexity: O(1)





