---
title: 3-Rotate-Matrix
updated: 2022-04-06 15:37:37Z
created: 2022-04-05 11:30:47Z
---

## **Rotate Matrix**

<ins>**Level**: Hard</ins>

An image is nothing but a matrix of pixels. Rotate a square image
by 90 degrees, given an array of pixels as integers. For example,

1 2 3       7 4 1
4 5 6 --> 8 5 2
7 8 9       9 6 3

Questions to Clarify:
Q.
A.

## Solution

**Pseudocode**:

```
performMove(int[][] a, r1, c1, r2, c2, offset)
    int temp = a[r1][c1 + offset];
    a[r1][c1 + offset] = a[r2 - offset][c1];
    a[r2] - offset[c1] = a[r2][c2 - offset];
    a[r2][c2 - offset] = a[r1 + offset][c2];
    a[r1 + offset][c2] = temp;

size = a.length // size of square
for i: 0 to (a.length/2 -1)
    r1 = i, c1 = i, r2 = r1 + size -1, c2 = c1 + size -1
    for j -> 1 to c2 -c1
        preformMovw(a, r1, c1, r2, c2, j)
    size -= 2
```

<ins>Test Cases:</ins>
Edge Cases: empty array, non square array
Base Cases: single element, 4 elements
Regular Cases: odd length array, even lenth array

Time Complexity: O(n), where n is the total elements in 2D array
Space Complexity: O(1)

**code:**

```java
private static void performMove(int[][] a, int r1, int c1, int r2, int c2, int offset) {
    int temp = a[r1][c1 + offset];
    a[r1][c1 + offset] = a[r2 - offset][c1];
    a[r2] - offset[c1] = a[r2][c2 - offset];
    a[r2][c2 - offset] = a[r1 + offset][c2];
    a[r1 + offset][c2] = temp;
}

public static int[][] rotateMatrixBy90(int[][] a) {
    if (a == null || a.length == 0 || a.length != a[0].length)
        return a;

    int size = a.length;
    for (int i = 0; i < a.length/2; i++) {
        int r1 = i, c1 = i, r2 = r1 + size -1, c2 = c1 + size -1;
        for (int j = 1; j <= size - 1; j++) {
            perfromMove(a, r1, r2, c2, j);
        }
    }
    return a;
}
```