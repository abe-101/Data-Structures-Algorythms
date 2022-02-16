## Traversing Array in Reverse 

**Level**: Easy

Given an array of numbers, replace each even number with two
of the same number. e.g, [1,2,5,6,8, , , ,] -> [1,2,2,5,6,6,8,8].  
Assume that the array has the exact amount of space to accommodate the result.

Questions to Clarify:
Q. How do you want to return the result?
A. modify the input array

Q. What would an empty element contain?
A. -1

## Solution
Traverse the array backwards with two pointer. Pointer end set at the length of the array and i at the last filled element (using a helper function). While i >= 0 If i is even decrement end and move a[i] to a[end] and repeat. Else if i is odd decrement end and move a[i] to a[end]

**Pseudocode**:
```
end = a.length
i = last filled element (helper function)
while i >= 0
    if (a[i]%2 == 0)
        a[--end] = a[i]
    a[--end] = a[i]
    i--
```
**Test Cases**:
Corner Case - null, empty array, array with only blanks
Base Case - one odd number, one even number
Regular Case - only odd numbers, only even numbers, both odd and even numbers

Time Complexity: O(n) aka linear time
Space Complexity: O(1) aka constant space





