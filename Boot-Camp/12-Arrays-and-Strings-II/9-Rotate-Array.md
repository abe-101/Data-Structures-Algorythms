---
title: 9-Rotate-Array
updated: 2022-04-07 13:27:14Z
created: 2022-04-07 13:17:07Z
tags:
  - easy
  - subarray
---

## **Rotate Array**

<ins>**Level**: Easy</ins>
Rotate an array A by X items.
For example,
A = [1,2,3,4,5,6] and X = 2, Result = [5,6,1,2,3,4]
Hint​: Use same trick we used in "Reverse Words of a Sentence".

Questions to Clarify:
Q. Can ​X​ be greater than the length of the array?
A. Yes

## Solution
Let's first assume that ​X ​is less than ​A.length​.
To rotate the array by ​X​, we can do the following:
1. Reverse the entire array.
2. Reverse the first ​X​ elements.
3. Reverse the rest of the elements.
This is the result - A rotated by 2. Now, how do we handle ​X >= A.length​.
Let's say ​X = A.length​. In our example, the result will be ​A​ itself - ​[1,2,3,4,5,6]
When we rotate by ​A.length​, ​A​ comes back to the original array. So we can just
find the remainder of​ X/A.length​, and rotate the array by that number. In other words, rotate by
X%A.length​.

**Pseudocode**:
```
result(int[] a, int X)
    x = x % a.length
    reverse a
    reverse a from 0 to x-1
    reverse a from x to a.length-1
```
<ins>Test Cases:</ins>
Edge Cases: empty array, null array
Base Cases: single element, two elements
Regular Cases: multiple elements (X=0, X<A.length, X>=A.length)

Time Complexity: O(n)
Space Complexity: O(1)

**code:**
```java
public static void rotate(int[] a, int x) {
    x = x % a.length;
    
    reverse(a, 0, a.length - 1);
    reverse(a, 0, x - 1);
    reverse(a, x, a.length - 1);
}

private static void reverse(int[] a, int start, int end) {
    int low = start, high = end;
    while (low < high) 
        swap(a, low--, high--);
    }
}

// helper code
private static void swap(int[] a, int i, int j) {
    int temp = a[j];
    a[j] = a[i];
    a[i] = temp;
}
```
