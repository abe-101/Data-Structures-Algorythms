---
title: 3-Print-Combos
updated: 2022-03-08 16:38:00Z
created: 2022-03-07 15:24:09Z
---

## Print Combos

Given an array of integers, print all combinations of size X.

**Level**: Medium

Questions to Clarify:
Q. Can the array have duplicates?
A. No, you can assume there are no duplicate numbers.

Q. What to print if X is greater than the size of the array?
A. Print nothing, as there will be no valid combinations.

Q. What to print if the array is empty?
A. Print nothing as there will be no combinations.

## Solution

We use a buffer of size X with a recursive function "printCombosHelper".
In any recursive call to printCombosHelper(), the buffer is filled up to a certain index i+1, and the task for the function call to fill index i. If i is greater the size of the buffer, then the buffer is full and we print its contents.

Otherwise, we find the candidates from the input array that can go into index i. We place each candidate into index i and then call printCombosHelper() for i+1

**Pseudocode**:

```
printCombos(a, x)
    buffer = new array of sixe x
    printCombosHelper(a, buffer, 0, 0)

printCombosHelper(a, bufferr, startIndex, bufferIndex):
    if buffer is full
        print buffer
        return

    if startIndex is out of bounds
        return
    
    for i: startIndex to a.length-1
        place a[i] into buffer[bufferIndex]
        printCombos(a, buffer, i + 1, bufferIndex + 1)
```

**Test Cases**:
Edge Cases: a is empty/null, X is 0, X is greater than a.length
Base Cases: a is of size 1 and 2, X is 1
Regular Cases: X is smaller than a.length, X is equal to a.length

Time Complexity:
Space Complexity:

**code:**

```java
public static void printCombos(int[] a, int x) {
    if (a == null || a.length == 0 || x > a.length)
        return;

    int[] buffer = new int[x];
    printCombosHelper(a, buffer, 0, 0);
}

public static void printCombosHelper(int[] a, int[] buffer, int startIndex,
        int bufferIndex) {
    // termination cases - buffer full
    if (bufferIndex == buffer.length) {
        for (int i = 0; i < buffer.length; i++) {
            System.out.print(buffer[i]);
        }
        System.out.println();
        return;
    }
    if (startIndex == a.length) {
        return;
    }

    // find candidates that go into current buffer index
    for (int i = startIndex; i< a.length; i++) {
        // place item into buffer
        buffer[bufferIndex] = a[i];

        // recurse to next buffer index
        printCombosHelper(a, buffer, i + 1, bufferIndex + 1);
    }
}
```