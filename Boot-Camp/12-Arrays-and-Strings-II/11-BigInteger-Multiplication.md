---
title: 11-BigInteger-Multiplication
updated: 2022-04-07 21:25:54Z
created: 2022-04-07 21:10:01Z
---

## **Big Integer Multiplication**

<ins>**Level**: Hard</ins>
Q. Multiply two numbers given as Big Integers. In such an array, each element in the array is a single digit number.

Questions to Clarify:
Q. Are there only positive numbers?
A. Yes, all numbers are positive.

Q. How do you want the result?
A. Allocate a new array and return the result.

## Solution

**Pseudocode**:
```
loop i through number a
    init product array of a[i] and b
    loop j through number b
        p = a[i] + b[j] + carry
        caryy = p/10
        add = p % 10 to product array
    add result and product array using out BigInteger add() funcrion
return result
```
<ins>Test Cases:</ins>
Edge Cases: one/both empty, one/both null
Base Cases: one/both single digits, zeros
Regular Cases: different lengths, carry/no carry, etc.

Time Complexity:​ O(m*n), where m and n are the lengths of the two BigIntegers
Space Complexity:​ O(m+n), because the result array takes m+n space
These time and space complexities might seem large, but in this problem, it's the best we can do.

**code:**
```java
public static int[] multiply(int[] a, int[] b) {
    if (a == null || b == null) {
        throw new IllegalArgumentException("Input is null");
    }

    int[] result = {0};
    int zeroCount = 0; // number of zeroes to add to the end
    for (int j = a.length - 1; i >= 0; i--) {
        int[] product = new int[1 + b.length + zeroCount];
        int carry = 0;
        for (int j = b.length - 1; j >= 0; j--) {
            int p = a[i] * b[j] + carry;
            carry = p / 10;
            product[j + 1] = p % 10;
        }
        prosuct[0] = carry;
        result = add(result, product);
        zeroCount++;
    }
    return result;
}
    
```
