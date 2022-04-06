---
title: 1-Max-Diff
updated: 2022-04-04 19:26:56Z
created: 2022-04-04 15:57:05Z
---

## **Max Diff**

<ins>**Level**: Medium</ins>

Questions to Clarify:
Q. Are the stock prices given as integers or can they be a double/float?
A. Integers

Q. How do you want the result?
A. Return the maximum amount of money you can make.

## Solution

This is a very common technique, one you should practice a few times.
The Max Diff is the maximum difference between two elements in an array, with the lesser element coming before the greater element.
For example:
\[9,3,2,​1​,5,7,2,​8​,3,4\] -> Max diff is 7, from 1 and 8.
Notice that the difference between 9 and 1 is higher, but it doesn't count because 1 comes after 9.
Stock trade is a perfect application of this algorithm. To make money from a normal trade, you need to buy at a lower price and sell at a higher price.
To find the max diff, you keep the minimum element encountered so far (​min\_so\_far​). And that’s all.
If you find that the current element is farthest from ​min\_so\_far​, that makes the new max diff.

**Pseudocode**:

```
min_so_far = Infinity
max_diff = 0
for i: 0 to a.length
    if a[i] < min_so_far
        set a[i] as the new min_so_far

    if (a[i] - min_so_far) > max_diff
        new max_diff is a[i] - min_so_far

return max_diff
```

<ins>Test Cases:</ins>
Edge Cases: empty array, null array
Base Cases: one item in array, 2 items in array (increasing/decreasing/equal)
Regular Cases: stock price sorted (asc/desc), normal case

Time Complexity: O(n)
Space Complexity: O(1)

**code:**

```java
public static int oneTrade(int[] prices) {
    if (prices == null || prices.length < 2) {
        return 0;
    }
    
    int minSoFar = Integer.MAX_VALUE;
    int maxDiff = 0;

    for (int i = 0; i < prices.length; i++)
        minSoFar = Math.min(minSoFar, prices[i]);
        maxDiff = Math.max(prices[i] - minSoFar, maxDiff);
    }

    return maxDiff;
}
```