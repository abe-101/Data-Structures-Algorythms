---
title: 6-Is-Rotation
updated: 2022-04-06 19:11:17Z
created: 2022-04-06 18:55:15Z
tags:
  - easy
  - substring
---

## **Is Rotation**

<ins>**Level**: Easy</ins>

Questions to Clarify:
Q. How do you want the result?
A. Return a boolean (true/false).

Q. What if both Strings are equal?
A. Return true.

## Solution

This trick is a simple use of strings. It goes as follows:

1.  Concatenate a string to itself: ​"canada” → "canadacanada"
2.  Check if the other string is a substring of this concatenated string.
    For example,
    "dacana"​is a substring of ​"canadacanada"​, hence it is a rotation.
3.  This will only work if both strings are of equal size. Otherwise, they can’t be rotations of one another.

**Pseudocode**:

```
string concat = a + a;
return concat.catains(b)
```

<ins>Test Cases:</ins>
Edge Cases: empty string, null string, invalid input
Base Cases: length 1, length 2, length different for both
Regular Cases: equal strings, rotation by 1, rotation by n

Time Complexity: O(n)
Space Complexity: O(n)

**code:**

```java
public static boolean isRotation(String a, String b) {
    if (a == null || b == null || a.length() != b.length())
        return false
    
    return (a+a).contains(b);
}
```