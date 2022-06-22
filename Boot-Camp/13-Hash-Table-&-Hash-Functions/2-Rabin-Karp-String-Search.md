---
title: 2-Rabin-Karp-String-Search
updated: 2022-04-10 20:39:59Z
created: 2022-04-10 20:09:26Z
---

## **Rabin Karp String Search**

<ins>**Level** Hard:</ins>
String Search: Find the index where the larger string A contains a target string T.

Questions to Clarify:
Q. If T occurs multiple times in A, do you want just the first index?
A. Yes

Q. If T doesn't exist in A, can I return -1?
A. Yes

Q. If T is empty, does that mean it exists in A?
A. Yes, empty strings exist in any non-null string.

Q. What if S or T are null?
A. Throw a null pointer exception.

## Solution

**Pseudocode**:
```
search(S, T)
    if T or S is null, throw exception
    if size(T) > size(S), return -1
    if T is empty, return -1

    // process first T characters
    hashT = 0   // hash of T
    hash = 0    // sliding window hash
    for i: 0 to T.length -1
        add T[i] to hashT
        add S[i] to hash
    if hashT == hash
        return 0

    for i: T.length to S.length - 1
        remove S[i - T.length] from hash, add S[i] to hash
        if hash == hashT
            Target found, return i - T.length

    Target not found, return -1
```
<ins>Test Cases:</ins>
Edge Cases: size(T) > size(S), T is empty/null, S is empty/null
Base Cases: T is 1 char, S is 1 char
Regular Cases: T is at S[0], T is at end, T is in middle

Time Complexity: O(n)
Space Complexity: O(1)
**code:**
```java
public static int search(String str, String target) {
    if (str == null || target == null)
        throw new NullPointerException();

    if (target.isEmpty()    // empty string exists in every string
        return 0;
    if (target.length() > str.length())
        return -1;

    int x = 53;     // a prime number

    // calculate hash for first target.length letters
    int hashT = 0;
    int hash = 0;
    for (int i = 0; i < target.length(); i++) {
        hashT = hashT * x + target.charAt(i);
        hash = hash * x + str.charAt(i);
    }
    // found match in first substring
    if (hashT == hash && target.equals(str,substring(0, target.length())))
        return 0;
    // calculate x^(t.length - 1) beforehand. Notice we didn't use the inbuilt
    // Math.pow() function. This is because it does not wrap around integers if
    // they overflow. If an integer goes past ~2 billion, our code goes back to
    // 0 and counts from there. This is the behavior we want. Math.pow()
    // considers the number to be infinity instead of counting from 0 again.
    int cPow = 1;
    for (int i = 0; i < target.length() - 1; i++) {
        xPow *= x;
    }

    for (int i  = target.length(); i < str.length(); i++) {
        int toRemove = str.charAt(i - target.length());
        hash = ((hash - tpRemove * xPox) * x + str.charAt(i);
        if (hash == hashT
                && target.equals(str.substring(i - target.length() + 1, i + 1))) {
            return i - target.length() + 1;
        }
    }
    return -1; // not found
}           
```
