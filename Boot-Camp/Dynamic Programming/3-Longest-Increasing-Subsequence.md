---
title: 3-Longest-Increasing-Subsequence
updated: 2022-03-30 16:19:09Z
created: 2022-03-30 15:49:59Z
---

## **Longest Increasing Subsequence**

Longest Increasing Subsequence: Given an array of integers, find the length of the longest increasing subsequence.
For e.g, in [1, 3, 2, 5, 3, 5, 6], the longest increasing subsequence is [1, 2, 3, 5, 6] of length 5.

<ins>**Level**: Hard</ins>

Questions to Clarify:
Q. What if the array is null or empty?
A. The length would be 0.

Q. Is an empty subsequence considered? Or should each subsequence have at least one number?
A. A subsequence needs to have at least one element.

## Solution
We keep track of the LIS (longest increasing subsequence) for each element. now we can figure out the LIS of i+1 by taking a look at all LIS for j: 0 .. i if a[j] is less than a[i+1] then there is a possibility of a LIS from j.
The lengthof this candidate will be LIS[j] + 1.

**Pseudocode**:
```
LIS(int[] a):
    result = 1
    for i: 0 to a.length-1:
        LIS[i] = 1
        for j: 0 to i-1 {
            if (a[j] is smaller than a[i]) {
                LIS[i] = max(LIS[i], LIS[j] + 1)
            }
        }
        result = max(result, LIS[i])
    ]
    return result

```
<ins>Test Cases:</ins>
Edge Cases: empty array, null array
Base Cases: single element
Regular Cases: sorted array (increasing, decreasing), unsorted array

Time Complexity: O(n^2)
Space Complexity: O(n)

**code:**
```java
public static int longestIncreasingSubsequence(int[] a) {
    if (a == null || a.length == 0)
        return 0;

    int[] longest = new int[a.length];
    int result = 1;
    for (int i = 0; i < a.length; i++) {
        longest[i] = 1;
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i]) {
                longest[i] = Math.max(longest[i], longest[j] + 1);
            }
        }
        result = Math.max(result, longest[i]);
    }

    return result;
}
```
