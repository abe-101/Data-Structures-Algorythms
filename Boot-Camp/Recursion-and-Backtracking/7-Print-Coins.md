---
title: 7-Print-Coins
updated: 2022-03-08 17:47:23Z
created: 2022-03-08 17:31:42Z
---

## Print Coins

**Level**: Medium

Coin Change Problem: Given a set of coin denominations, print out the different ways
you can make a target amount. You can use as many coins of each denomination as you like.
For example: If coins are [1,2,5] and the target is 5, output will be:
[1,1,1,1,1]
[1,1,1,2]
[1,2,2]
[5]

Questions to Clarify:
Q. Does [1,2] and [2,1] count as one, i.e, do we care about permutations?  
A. No, we only care about combinations, so [1,2] and [2,1] will count as the same.  

Q. Can we assume that all coins will be integers greater than 0?  
A. Yes  

## Solution
This problem is similar to generating combinations, except that a number can be repeated several times. So, while picking candidates that go into the buffer, we will also consider the previous candidate that went in.
Note: In this solution, we are using a stack as a buffer. You can also use an array of size target.

**Pseudocode**:
```
printCoinsHelper(coins, target, stack buffer, startIndex, currentSum)
    if currentSum > target
        return
    if currentSum == target // we found an answer
        print buffer
        return

    for i: startIndex to coins.length
        place coin into buffer
        // recurse
        printCoinsHelper(coins, target, buffer, i, currentSum + coins[i])
        remove coin from buffer
```
**Test Cases**:
Edge Cases: Coins array is null/empty, Target is 0 or -ve.  
Base Cases: Coins array is size 1  
Regular Cases: Target is equal to a coin, target is greater than all coins  

STime Complexity: Factorial Complexity  
pace Complexity:i Space Complexity: O(Target), because in the worst case, both our buffer and the recursion
stack will be the size of the target. (if we use all 1's to make target)


**code:**
```java
public static void printCombos(int[] coins, int target) {
    if (coins == null || coins.length == 0 || target <= 0)
        return;

    printCoinsHelper(coins, target, 0, new Stack<Integer>(), 0);
}

public static void printCoinsHelper(int[] coins, int target, int startIndex,
        Stack<Integer> buffer, int sum) {
    // termination cases - buffer full
    if (sum > target)
        return;
    if (sum == target) {
        print(buffer)
        return;
    }

    // find candidates that go into current buffer index
    for (int i = startIndex; i < coins.length; i++) {
        // place item into buffer
        buffer.push(coins[i]);
        // recurse to next buffer index
        printCoinsHelper(coins, target, i, buffer, sum + coins[i]);
        buffer.pop();
    }
}
```
