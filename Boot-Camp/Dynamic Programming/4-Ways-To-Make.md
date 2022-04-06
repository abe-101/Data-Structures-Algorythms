---
title: 4-Ways-To-Make
updated: 2022-03-30 17:07:21Z
created: 2022-03-30 15:50:10Z
---

## **Ways To Make**

<ins>**Level**: Hard</ins>

Coin Change - Print Count: Given a set of coin denominations, print out the number of ways you can make a target amount.
You can use as many coins of each denomination as you like.
For example: If coins are [1,2,5] and the target is 5, the different ways are:

[1,1,1,1,1]
[1,1,1,2]
[1,2,2]
[5]

The Output will be 4.

Questions to Clarify:
Q. We are considering combinations and not permutations, correct? For example, [1,2,2] and [2,2,1]are considered the same?
A. Correct, we want combinations.

## Solution

**Pseudocode**:
```
int[] a = new int[n+1];
a[0] =1;

for (int coin : coins) {
    for (int i = coin; i <= n; i++) {
        a[i] = a[i] + a[i-coin];
    }
}
return a[n];
```
<ins>Test Cases:</ins>
Edge Cases: Target amount is 0, 1
Base Cases: one coin only
Regular Cases: multiple coins

Time Complexity: O(Amount*Coins)
Space Complexity: O(Amount)

**code:**
```java
public static int waysToMake(int amount, int[] coins) {
    int[] a = new int[amount+1];
    a[0] = 1;

    for (int coin : coins) {
        for (int i = coin; i <= amount; i++) {
            a[i] = a[i] + a[i-coin];
        }
    }
    return a[amount];
}
```
