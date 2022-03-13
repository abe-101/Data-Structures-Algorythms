---
title: 6-Print-Permutations
updated: 2022-03-11 14:50:37Z
created: 2022-03-08 15:32:20Z
---

## Print Permutations

**Level**: Medium

Given an array A, print all permutations of size X.
For example,
Input:
A = \[1,2,3\]
X = 2
Output:
\[1, 2\]
\[1, 3\]
\[2, 1\]
\[2, 3\]
\[3, 1\]
\[3, 2\]

Questions to Clarify:
Q. Can we assume there are no duplicates?
A. Yes

Q. If the input is an empty array, do we just print nothing?
A. Yes

Q. If the input is null, should we throw an exception of simply print nothing?
A. Let's just print nothing.

## Solution

While computing combinations, we went forward from the previous number. So if we are in the following situation:
X = 3
A = \[1,2,3,4,5,6,7\],
Buffer = \[1,4, \] (index 2 is empty)
We start filling index 2 with 5, 6 and 7.
For permutations, however, we can fill index 2 with any number except 1 and 4. This is because
\[1,4,2\] and \[1,2,4\] are different permutations.
So, we need to keep track of which numbers are already in our buffer. Our candidates for
buffer index 2 will be all the other numbers.

**Pseudocode**:

```
printPermsHelper(a, buufer, bufferIndex, isInBuffer)
    if buffer is full
        print buffer
        return

    for i: 0 to a.length-1
        if (isInBuffer[i] is false) // index is not in buffer
            place index i in buffer
            mark isInBufffer[i] to true
            // recurse to next level
            printPerHelper(a, buffer, bufferIndex + 1, isInBuffer)
            mark isInBuffer[i] to false
```

**Test Cases**:
Edge Cases: a is empty/null, X is 0, X is greater than a.length
Base Cases: a is of size 1 and 2, X is 1
Regular Cases: X is smaller than a.length, X is equal to a.length

Time Complexity:
Space Complexity: O(N), where N is A.length. We use O(N) space both in the buffer allocation

**code:**

```
public static void printPerms(int[] a, int x) {
    if (a == null || a.length == 0 || x > a.length)
        return;

    int[] buffer = new int[x];
    boolean[] isInBuffer = new boolean[a.length];
    printCombosHelper(a, buffer, 0, isInBuffer);
}

public static void printPermsHelper(int[] a, int[] buffer, int bufferIndex, boolean[] isInBuffer) {
    // termination cases - buffer full
    if (bufferIndex == buffer.length) {
        for (int i = 0; i < buffer.length; i++) {
            System.out.print(buffer[i]);
        }
        System.out.println();
        return;
    }

    // find candidates that go into current buffer index
    for (int i = 0; i < a.length; i++) {
        if (!isInBuffer[i]) {
            // place item into buffer
            buffer[bufferIndex] = a[i];
            isInBuffer[i] = true;
            // recurse to next buffer index
            printCombosHelper(a, buffer, i + 1, isInBuffer);
            isInBuffer[i] = false;
        }
    }
}
```