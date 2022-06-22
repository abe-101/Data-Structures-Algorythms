---
title: 1-Polynomial-Hash-Funtion
updated: 2022-04-10 19:29:32Z
created: 2022-04-10 19:19:32Z
---

## **Polynomial Hash Function**

<ins>**Level**: Hard</ins>
Generate a good hash function for a String.

## Solution
Hash functions are basic building blocks of hash-based data structures. Interviewers are generally mpressed if you have knowledge of good hash functions.
For strings, we generate hash functions as a polynomial:
hash("goat") => 'g'.x​3​ + 'o'.x​2​ + 'a'.x + 't'
Note that these are the integer values of the characters.
We need to assign an integer value to ​x​. Prime numbers are known to make good values for ​x​.
The mathematical proof of this is beyond the scope of an interview. We use 53 in the code below.
**Pseudocode**:
```
find hash(string s)
    int hash = 0. x = 53
    for i: 0 to s.length - 1
        hash = hash * x + s[i];
    return hash;
```
<ins>Test Cases:</ins>
Edge Cases: empty string, null string
Base Cases: string with 1 character
Regular Cases: try same string twice, should return the same hash code

Time Complexity: O(n)
Space Complexity: O(1)

**code:**
```java
public static int hash(String str) {
    int hash = 0, x = 53;
    for (int i = 0; i < str.length (); i++) {
        hash = hash * x +str.charAt(i);
    }
    return hash;
}
```
