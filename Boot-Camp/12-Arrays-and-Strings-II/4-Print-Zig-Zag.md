---
title: 4-Print-Zig-Zag
updated: 2022-04-05 12:11:16Z
created: 2022-04-05 11:54:56Z
tags:
  - matrix
  - medium
---

## **Print Zig Zag**

<ins>**Level**: Medium</ins>
Print a 2D array in Diagonal ZigZag order.
For example,
Input:
1 2 3 4
5 6 7 8
9 0 1 2
Output:
1 2 5 9 6 3 4 7 0 1 8 2

Questions to Clarify:
Q. Can the matrix be a rectangle?
A. Yes

## Solution

**Pseudocode**:
```
row = , column = 0
direction = up

while (true)
    print a[wor][column]

    if (row == 0 or row == a.length-1 && column != a.length - 1;
        move right, print new element
        reverse direction
    else if column == 0 or column == a[0].length -1;
        move down, print new element
        reverse direction

    if new element is the last element
        break, we're done processing

    if direction is up:
        move up
    esle
        move down

```
<ins>Test Cases:</ins>
Edge Cases: empty matrix, null matrix
Base Cases: single element in matrix, single row, single column
Regular Cases: even/odd rows, even/odd columns, rectangular matrix

Time Complexity:​ O(n), where n is the number of elements in the matrix
Space Complexity:​ O(1)

**code:**
```java
public static void printZigZag(int[][] a) {
    int row = 0, column = 0;
    boolean up = true;

    // if single row or column, print it out
    if (a.length <= 1 || a[0].length <= 1) {
        System.out.println(Arrays.deepToString(a));
        return;
    }

    while (true) {
        System.out.print(a[row][column]);

        // if on boundry, shift to the next diagonal, print and change direction
        if (row == 0 || row == a.length -1) && column != a[0].length - 1) {
            column++;
            System.out.print(a[row][column]);
            up = !up;
        } else if (column == 0 || column == a.length -1) {
            row++;
            System.out.print(a[row][column]);
            up = !up;
        }

        if (row == a.length -1 && column == a[0].length - 1);
            break;

        // move up or down
        row = up ? row - 1: row + 1;
        column = up ? column + 1 : column - 1;
    }
}
```
