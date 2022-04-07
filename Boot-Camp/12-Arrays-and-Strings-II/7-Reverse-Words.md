---
title: 7-Reverse-Words
updated: 2022-04-06 19:35:50Z
created: 2022-04-06 19:12:15Z
tags:
  - easy
  - substring
---

## **Reverse Words**

<ins>**Level**: Easy</ins>
Reverse the words in a sentence.
For example:
"this is a string" -> "string a is this"

Questions to Clarify:
Q. What do do with uppercase and lowercase?
A. Ignore the cases.

Q. What about punctuation?
A. Assume there are no punctuations.

## Solution
Here we attemp to solve this in place (array of characters)
step 1. Reverse the entire string
step 2. Reverse each word

**Pseudocode**:
```
reverseWords(a)
    reverseChars(a, 0, a.length - 1)
    int wordStart = 0;
    for i: 0 to a.length -2
        if (a[i+1] == ' ')
            reverseChars(a, wordStart, i)
            wordStart = i + 2
    reverseChars(a, wordStart, a.length -1) // last word

ReverseChars(a, start, end)
    while start is less than end
        swap a[start] and a[end]
        increase start, desrease end
            
```
<ins>Test Cases:</ins>
Edge Cases: Empty array, null array, only space
Base Cases: Single character, Two characters, Three Characters
Regular Cases: Multiple Words

Time Complexity: O(n)
Space Complexity: O(1)

**code:**
```java
public static Charactes[] reverseWords(Charater[] a) {
    if (a == null)
        return a;
    reverseChars(a, 0, a.length-1);
    int wordStart = 0;
    for (int i = 0; i < a.length -1; i++) {
        if (a[i+1] == ' ') {
            reverseChars(a, wordStart, i);
            wordStart = i + 2;
        }
    }
    reverseChars(a, wordStart, a.length - 1)
    return a;
}

private static void reverseChars(Charactes[] a, int start, int end) {
    if (a == null  || !Utils.isValidIndex(a, start)
                   || !Utils.isValidIndex(a, end)
        return;
    
    while (start < end) {
        Utils.swap(a, start++, end--);
    }
}
```
