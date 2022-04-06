---
title: 2-Climbing-Steps-Problem
updated: 2022-03-30 15:48:40Z
created: 2022-03-30 14:48:01Z
---

## **Climbing Steps Problem**
Let’s say you have to climb N steps. You can jump 1 step, 3 steps or 5 steps at a time. How many ways are there to get to the top of the steps.


## Bottom Up Approach using Tabulation

**Pseudocode**:
```
Init array a of sinze N
Init a[0] to 1
for i: 0 to a.length-1
    // ensure these are within bounds
    a[i + 1] = a[i + 1] + a[i];
    a[i + 3] = a[i + 3] + a[i];
    a[i + 5] = a[i + 5] + a[i];
last index of array will contain result
```

**code:**
```java
public static int waysToClimb(int n) {
    int[] a = new int[n+1];
    a[0] = 1;
    
    for (int i = 0; i < a.length; i++) {
        if (i + 1 < a.length)
            a[i + 1] += a[i]

        if (i + 3 < a.length)
            a[i + 3] += a[i]

        if (i + 5 < a.length)
            a[i + 5] += a[i]
    }
    return a[n];
}
```
Time Complexity​: O(N * 3) = O(N)
Space Complexity​: O(N)


## Top Down Approach using Tabulation

**Pseudocode**:
```
Init array a of sinze N
Init a[0] to 1
for i: 1 to a.length-1
    // ensure these are within bounds
    a[i] = a[i-1] + a[i-3] + a[i-5]
last index of array will contain result
```

**code:**
```java
public static int waysToClimb(int n) {
    int[] a = new int[n+1];
    a[0] = 1;
    
    for (int i = 1; i < a.length; i++) {
        int nMinus1 = i-1 < 0 ? 0 : a[i-1];
        int nMinus3 = i-3 < 0 ? 0 : a[i-3];
        int nMinus5 = i-5 < 0 ? 0 : a[i-5];

        a[i] = nMinus1 + nMinus3 + nMinus5;
    }

    return a[n];
}
```
Time Complexity​: O(N * 3) = O(N)
Space Complexity​: O(N)


