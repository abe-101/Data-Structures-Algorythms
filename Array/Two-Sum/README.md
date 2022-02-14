## Problem: Two Sum


**Level**: Easy

Given an array of integers, find a pair of integers that sums to a number Target.

For e.g, if A = [6,3,5,2,1,7]. Target = 4, Result= [3,1]

### Solution:

**Brute Force:**  

Pseudocode: 
```
for i: 0 to a.length-1
    for j: i+1 to a.length-1
        if a[i]+a[j] == target
            return new pair (a[i], a[j])

no pair found, return null
```

Time Complexity: O(n^2)  
Space Complexity: O(1)


**Using Hash Set:**

Pseudocode: 

initialize empty hash set
for i: 0 to a.legnth-1
    if target-a[i] is in hash set
        return new pair (a[i], target-a[i])
    else
        add a[i] to hash set

no pair found, return null

Time Complexity: O(n)  
Space Complexity: O(n)  

