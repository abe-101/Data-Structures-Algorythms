---
title: 8-Longets-Palindrome-Substring
updated: 2022-04-07 13:07:05Z
created: 2022-04-07 12:48:07Z
tags:
  - medium
  - substring
---

## **Longets Palindrome Substring**

<ins>**Level**:Medium</ins>
Find the longest palindrome in a sting. For example,

"ab​babab​aab" -> "babab"

Questions to Clarify:
Q. How do you want the output?
A. Return a pair of indices that represent start and end of the substring.

Q. Is a single character considered a palindrome?
A. Yes

## Solution
We look at odd length and even length palindromes.
odd length have a character in middle. For every i we "spread" out checking if both sides are equal.

for even length we look at the gaps in between elements.

**Pseudocode**:
```
Find odd palindrome
got through each character
    try expanding as much as possible
    compare with largest palindrome found so far
Do the same with even palindrome
```
<ins>Test Cases:</ins>
Edge Cases: empty string, null string
Base Cases: one character, 2 characters
Regular Cases: No palindrome, one palindrome, multiple palindromes

Time Complexity: O(n^2)
Space Complexity: O(1)

**code:**
```java
public static Pair<Integer> longestPalindrome(String a) {
    if (a == null || a.isEmpty()) 
        return null;
    char[] ch = a.toCharArray();

    int longest = 1;
    Pair<Integer> result = new Pair<Integer>(0,0);

    // odd
    for (int i = 0; i < ch.length; i++) {
        int offset = 0;
        while (isValidIndex(ch, i-1-offset) && isValidIndex(ch, i+1+offset)
                && ch[i-1-offset] == ch[i+1+offset]) {
            offset++;
        }
        
        int longestAtI = offset*2 + 1;
        if (longestAtI > longest) {
            longest = longestAtI;
            result = new Pair<Integer>(i-offset, i+offset);
        }
    }

    // even
    for (int i = 0; i < ch.length; i++) {
        int offset = 0;
        while (isValidIndex(ch, i-offset) && isValidIndex(ch, i+1+offset)
                && ch[i-offset] == ch[i+1+offset]) {
            offset++;
        }
        
        int longestAtI = offset*2;
        if (longestAtI > longest) {
            longest = longestAtI;
            result = new Pair<Integer>(i-offset+1, i+offset);
        }
    }

    return result;
}

private static boolean isValidIndex(char[] a, int i) {
    return i >= 0 && i < a.length;
}

```
