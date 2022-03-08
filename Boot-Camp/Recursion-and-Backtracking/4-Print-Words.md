---
title: 4-Print-Words
updated: 2022-03-07 20:12:54Z
created: 2022-03-06 18:57:37Z
---

## Print Words

**Level**: Medium

Phone Number Mnemonics: Given an N digit phone number, print all the strings that can be made from that phone number. Since 1 and 0 don't correspond to any characters, ignore them.

Questions to Clarify:
Q. Is the phone number of a specific size?
A. No, it can be of any size

Q. Can we assume that the input will have only digits?
A. Yes

Q. Does the string have to be a valid English word?
A. No, the string can be anything.

Q. How do we handle if phone number is empty or null?
A. Print nothing.

## Solution

This problem is a straightforward application of Recursion using Buffer. For each buffer index, the candidates would be the letters corresponding to the digit at that index.

For example, in the array "234", the candidates for index 0 are letters that correspond to 2 - A, B, C.

We simply place each candidate in the current buffer index and recurse to the next.

**Pseudocode**:

```
printWords(a)
    buffer = new array of size a.length
    printWordsHelper(a, buffer, 0, 0)

printWordsHelper(a, buffer, aIndex, bufferIndex)
    if buffer is full or aIndex is equal to a.length
        print buffer

    candidates = get letters for a[aIndex]

    if candidates is empty, it must be a 0 or 1
        continue to next index

    for each candidate
        place candidate at buffer[bufferIndex]
        printWordsHelper(a, buffer, aIndex + 1, bufferIndex + 1)
```

**Test Cases**:
Edge Cases: a is empty/null
Base Cases: a has one number, a has only 1's and 0's
Regular Cases: a with 1's and 0's, without 1's and 0's

Time Complexity: Exponential Complexity - O(4^n), where n is the size of the phone number.
At each function call, we can call at most 4 function calls. We do this at most N times, so the total
number of function calls is:
4 X 4 X 4 .. (n times), which is 4^n
Space Complexity: O(n), where n is the size of the phone number. The O(n) space is taken
both by the buffer and the call stack.

**code:**

```
public static void printWords(int[] phoneNumber) {
    if (phoneNumber == null || phoneNumber.length == 0)
        return;

    char[] buffer = new char[phoneNumber.length];
    printWordsHelper(phoneNumber, buffer, 0, 0);
}

public static void printWordsHelper(int[] a, char[] buffer, int aIndex,
        int bufferIndex) {
    // termination cases - buffer full
    if (bufferIndex >= buffer.length || aIndex >= a.length) {
        for (int i = 0; i < buffer.length; i++) {
            System.out.print(buffer[i]);
        }
        System.out.println();
        //printArray(buffer, bufferIndex);
        return;
    }

    // find canditates for buffer position
    char[] letters = getLetters(a[aIndex]);
    
    if (letters.length == 0) 
        printWordsHelper(a, buffer, aIndex + 1, bufferIndex);
    

    // place candidates in buffer
    for (char letter: letters) {
        buffer[bufferIndex] = letter;
        printWordsHelper(a, buffer, aIndex + 1, bufferIndex + 1);

    }
}

// Helper function
public static char[] getLetters(int digit) {
    switch(digit) {
        case 0: return new char[]{};
        case 1: return new char[]{};
        case 2: return new char[]{'a', 'b', 'c'};
        case 3: return new char[]{'d', 'e', 'f'};
        case 4: return new char[]{'g', 'h', 'i'};
        case 5: return new char[]{'j', 'k', 'l'};
        case 6: return new char[]{'m', 'n', 'o'};
        case 7: return new char[]{'p', 'q', 'r', 's'};
        case 8: return new char[]{'t', 'u', 'v'};
        case 9: return new char[]{'w', 'x', 'y', 'z'};
    }
    throw new IllegalArgumentException("Invalid digit " + digit);
}

```