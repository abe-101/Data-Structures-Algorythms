---
title: 5-Print-Spiral
updated: 2022-04-06 16:12:09Z
created: 2022-04-06 15:48:26Z
---

## **Print In Spiral**

<ins>**Level**: Medium</ins>
Print elements of a matrix in spiral order.

Questions to Clarify:
Q. Can the matrix be a rectangle?
A. Yes

## Solution
We use the concept of layers again - similar to rotating a matrix by 90 degrees.
For each layer, we print out the 4 sides. To do this, we pass the ​lastRow​ and ​lastColumn
of every layer. This helps us define the boundaries of the layer:
We can now print each side using the formula shown in the image above.

**Pseudocode**:
```
printSppiral(int[][] a)
    for (int layer = 0; layer <= a.length/2; layer++) {
        lastColumn = a[0].length-1-layer
        lastRow = a.length-1-layer

        printLayer(a, layer, lastColumn, lastRow)
    }

printLayer(int[][] a, int layer, int lastColumn, int lastRow)
    print top row
    print right column
    print bottom row
    print left column
```
<ins>Test Cases:</ins>
Edge Cases: empty matrix, null matrix
Base Cases: single element in matrix, single row, single column
Regular Cases: even/odd rows, even/odd columns, rectangular matrix

Time Complexity: O(n), where n is the number of elements in the matrix
Space Complexity: O(1)

**code:**
```java
public static void printSpiral(int[][] a) {
    if (a == null || a.length == 0)
        return;
    for (int layer = 0; layer <= a.length/2; layer++) {
        printLayer(a, layer, a[0].length-1-layer, a.length-1-layer);

    }
}

public static void printLayer(int[][] a, int layer, int lastColumn, int lastRow) {
    // single element in layer, print separately because other cases won't handle it
    if (lastColumn == layer && lastRow == layer)
        System.out.print(a[layer][layer]);

    for (int current = layer; current < lastColumn; current++) { // top row
        System.out.print(a[layer][current]);
    }

    for (int current = layer; current < lastRow; current++) { // right column
        System.out.print(a[current][lastColumn);
    }

    for (int current = lastColumn; current > layer; current--) { // bottom row
        System.out.print(a[lastRow][current]);
    }

    for (int current = lastRow; current > layer; current--) { // left column
        System.out.print(a[current][layer]);
    }
}
```
