---
title: 5-Print-Subsets
updated: 2022-03-10 21:03:37Z
created: 2022-03-08 15:07:33Z
---

## Print Subsets

**Level**: Medium

Given an array of integers A, print all its subsets.
For example:
Input: \[1, 2, 3\]
Output:
\[\]
\[1\]
\[2\]
\[3\]
\[1, 2\]
\[1, 3\]
\[2, 3\]
\[1, 2, 3\]

Questions to Clarify:
Q. Do we print out the empty set?
A. Yes

Q. Can we assume there are no duplicates?
A. Yes

Q. If the input is an empty array, do we just print out the empty set?
A. Yes

Q. If the input is null, should we throw an exception of simply print nothing?
A. Let's just print nothing.

## Solution

**Pseudocode**:

```
printSubsets(a)
    buffer = new array of size a.length
    printSubsetsHelper(a, buffer, 0, 0)

printSubsetsHelper(a, bufferr, startIndex, bufferIndex):
    print buffer
    
    if buffer is full
        return

    if startIndex is out of bounds
        return
    
    for i: startIndex to a.length-1
        place a[i] into buffer[bufferIndex]
        printsubsetsHelper(a, buffer, i + 1, bufferIndex + 1)
```

**Test Cases**:
Edge Cases: A is empty/null
Base Cases: A is of size 1 and 2
Regular Cases: A is of size greater than 2

Time Complexity:
Space Complexity: O(N), where N is A's length. We use O(N) space both in the buffer allocation and on
the recursion stack.

**code:**

```java
public static void printSubsets(int[] a) {
    if (a == null || a.length == 0)
        return;

    int[] buffer = new int[a.length];
    printSubsetsHelper(a, buffer, 0, 0);
}

public static void printSubsetsHelper(int[] a, int[] buffer, int startIndex,
        int bufferIndex) {
      for (int i = 0; i < bufferIndex; i++) {
     		System.out.print(buffer[i]);
    }
    System.out.println();
    
    // termination cases - buffer full
    if (bufferIndex == buffer.length) {
        return;
    }
    if (startIndex == a.length) {
        return;
    }

    // find candidates that go into current buffer index
    for (int i = startIndex; i < a.length; i++) {
        // place item into buffer
        buffer[bufferIndex] = a[i];

        // recurse to next buffer index
        printSubsetsHelper(a, buffer, i + 1, bufferIndex + 1);
    }
}
```