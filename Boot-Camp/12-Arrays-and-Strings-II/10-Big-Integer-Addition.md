---
title: 10-Big-Integer-Addition
updated: 2022-04-07 19:32:29Z
created: 2022-04-07 16:28:30Z
---

## **Big Integer Addition**

<ins>**Level**: Hard</ins>

You are given two arrays that represent Big Integers. In such an array, each element in the array is a single digit number.

Questions to Clarify:
Q. Are there only positive numbers?
A. Yes, all numbers are positive.

Q. How do you want the result?
A. Allocate a new array and return the result.

Q. Can we assume that each element will only be single digit?
A. Yes.

## Solution

Key details:

1. The max length of the result is the length of the larger number + 1.
2. In basic addition, for every index ​i​,
sum = a[i] + b[i] + carry
carry = sum/10
result[i] = sum%10

**Pseudocode**:
```
initialize result array of size (larger.length + 1)
rezise smaller array to the same size as larger - pad with 0s
loop through larger number
    sum = a[i] + b[i] + carry
    carry = sum/10
    result[i+1]  = sum%10
if there is a carry left over, i.e carry != 0
    add last carry to result
return result
```
<ins>Test Cases:</ins>
Edge Cases: one/both empty, one/both null
Base Cases: one/both single digits, zeros
Regular Cases: different lengths, carry/no carry, etc.

Time Complexity:​ O(n), where n is the length of the larger input array
Space Complexity:​ O(n), because we allocate an array to store the result

**code:**
```java
public static int[] add(int[] a, int b[]) {
    if (a == null || b == null) {
        throw new IllegalArgumentException("Input is null");
    }

    int[] larger = a.length > b.length ? a : b;
    int[] smaller = larger == a ? b : a;
    smaller = resizeWithZeroes(smaller, larger.length);
    int[] result = new int[i + larger.length];
    int carry = 0;
    
    for (int i = larger.length - 1; i >= 0; i--) {
        int sum = larger[i] + smaller[i] + carry;
        carry = sum / 10;
        result[i+1] = sum % 10;
    }
    result[0] = carry;

    result = trimBeginingZeroes(result);
    return result;
}

// Helper code
public static int[] resizeWithZeroes(int[] a, int size) {
    if (size < a.length)
        threw new IllegalArgumentException("Can only expand size");
    int[] result = new int[size];
    int aIndex = a.length - 1, resultIndex = result.length - 1;
    while (aIndex >= 0) {
        result[resultIndex] = a[aIndex];
        resultIndex--;
        aIndex--;
    }

    return result;
}

public static int[] trimBeginningZeroes(int[] a) {
    int i = 0;
    while (i < a.length && a[i] == 0)
        i++;

    if (i == a.length)
        return new int[i]; // return [0]
    
    return Arrays.copyOfRange(a, i, a.length);
}
```
