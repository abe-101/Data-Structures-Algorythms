---
title: 6-Unkwown-Length-Search
updated: 2022-03-03 22:57:30Z
created: 2022-03-01 20:21:37Z
tags:
  - binary search
  - medium
---

## Search Array of Unknown length

**Level**: Medium

You are given an array, but you don't know the length. Write a program to find
a target element in the array.

Questions to Clarify:
Q. What happens if we try to access an index that is out of bounds?
A. An exception is thrown

Q. How do you want the output?
A. Return the index of target.

Q. What to return if target is not found?
A. Return -1

## Solution

first we look for the end by doubling our guess's. 0, 2, 4, 8, 16, ... this will triger an exception in log(n) steps. we know now that it lies within a\[i/2\] and a\[i\]. We can perform binary serch on thoes to find the end. oncle we now the length we can do a regular binary search to find the target.
One more thing to note. while not btter than O(log(n), we van make it more efficient. back in the first step if if a\[i\] is greater than target then you know that target is between a\[i/2\] and a\[i\].

**Pseudocode**:

```
high = 1
lastIndex = -1
while True
    if a[high] throws exception
        binary search over (high/2+1, high) for last LastIndex of the array
        break loop
    else
        high = high * 2
binary search from 0 to lastIndex for target element.
```

**Test Cases**:
Edge Cases: empty array, null array
Base Cases: single element, two elements
Regular Cases: power of 2 +- 1 / not a power of 2

Time Complexity: O(log(n))
Space Complexity: O(1)

**code:**

```
public static int findUnknownLength(int[] a, int target) {
    if (a == null || a.length == 0) {
        return -1;
    }

    int high = 1;
    int lastIndex = -1;

    // Consider putting a sanity limit here, for e.g. don't go more
    // than index 1 million. Discuss this with the interviuwer.
    while (true) {
        try {
            int temp = a[high];
        } catch (ArrayIndexOutOfBoundsException e) {
            lastIndex = binarySearchForLastIndex(a, high/2, high);
            break;
        }
        high *= 2;
    }

    return binarySearchOverRange(a, target, 0, lastIndex);
}

private static int binarySearchForLastIndex(int[] a, int low, int high) {
    while (low <= high) {

        int mid = low + (high - low)/2;
        try {
            int temp = a[mid];
        } catch (ArrayIndexOutOfBoundsException e) {
            // mid is out of bounds, go to lower half
            high = mid - 1;
            continue;
        }

        try {
            int temp = a[midi+1];
        } catch (ArrayIndexOutOfBoundsException e) {
            // mid + 1 is out of bounds, mid is last index
            return mid;
        }

        // both mid and mid + 1 are inside array, mid is not last index
        low = mid + 1;
    }

    return -1; // this subarray does not have end of the array
}

private static int binarySearchOverRange(int[] a, int target, int low, int high)
{
   while (low <= high) {
       int mid = low + ((high - low)/2);
       if (a[mid] == target) {
           return mid;
       } else if (a[mid] < target) {
           low = mid + 1;
       } else {
           high = mid - 1;
       }
   }

   return -1;
}

```