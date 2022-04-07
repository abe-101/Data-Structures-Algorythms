---
title: 2-Two-Trades
updated: 2022-04-07 13:28:29Z
created: 2022-04-04 18:57:37Z
tags:
  - hard
  - max diff
---

## **Two Trades**

<ins>**Level**: Hard</ins>

Questions to Clarify:
Q. Can the trades overlap?
A. No, the trades cannot overlap, i.e, you can not have 2 trades going on at one price.

Q. Can you make just one trade if that makes the maximum money?
A. Yes, you can have at most 2 trades.

Q. Are the stock prices given as integers or float?
A. Integers

Q. How do you want the result?
A. Return the maximum amount of money you can make.

## Solution

We are going to build on top of the Max Diff technique, and extend it further. This is why it is very important to learn these techniques. We recommend writing them on paper 3 or more
times. Get comfortable with these techniques and you can build upon them.
Let’s say we have an array of prices. We introduce idea of best trade ​up to​ ​i​.
This is the most money we can make with one trade, given the subarray ​prices\[0..i\]​.
We can create this ​best\_till\_i​ array for each ​i​ in O(n) time and O(n) space.
Now, let’s say we create another array ​best\_from\_i​, which is the most money we can make
starting at ​i​. I.e, with the subarray ​prices\[i..prices.length-1\]
Now, to find the maximum of 2 trades over the entire price array:
for i -> 0 to prices.length
max\_2\_trades = Max(max\_2\_trades, best\_till\_i\[i\] + best\_from\_i\[i+1\])
This may not be very intuitive at first. Most people will not be able to come up with the perfect solution
in the space of an interview. However, since you may be expected to come up with this, it is useful to
know the building blocks of this technique.

**Pseudocode**:

```
1. create best_till_i array
apply max_diff, stroe max_diff at each i in best_till_i

min_so_far = Infinity
max_diff = 0
for i: 0 to a.length
    if a[i] < min_so_far
        set a[i] as the new min_so_far

    if (a[i] - min_so_far) > max_diff
        new max_diff is a[i] - min_so_far

    best_till_i[i] = max_diff // stores max money you can make until i

2. Now for the tricky part - create best_from_i array. We apply the max diff
algorithm in reverse. We iterate from the end of the array and find the max
diff, or in this case, the max drop.

apply max_diff in reverse:
max_so_far = -Infinity
max_diff = 0
for i: a.length-1 to 1
    if a[i] > max_so_far
        set a[i] > max_so_far

    if (max_so_far - a[i] > max_diff)
        new max_diff is max_so_far - a[i]

    best_from_i[i] = max_diff // store the max money you can make starting from i

3. Find the maximun money with 2 trades

for i: 0 to prices.length-1
    max_2_trades = Max(max_2_trades, best_till_i[i] +  best_from_o[i+1])
```

<ins>Test Cases:</ins>
Edge Cases: empty array, null array
Base Cases: one element, 2 elements (sorted asc/desc/equal)
Regular Cases: sorted asc/desc/equal, min and max at the ends of the array, normal cases.

Time Complexity: O(n)
Space Complexity: O(n)

**code:**

```java
public static Integer twoTrades(Integer[] prices) {
    if (prices == null || prices.length < 2)
        return 0;
    
    int[] bestTill = int[prices.length];
    int minSoFar = Integer.MAX_VALUE, maxDiff = 0;
    for (int i = 0; i < prices.length; i++) {
        minSoFar = Math.min(minSoFar, prices[i]);
        MaxDiff = Math.max(maxDiff, prices[i] - minSoFar)
        bestTill[i] = maxDiff;
    }
    
    int[] bestFrom = new int[prices.length];
    int maxSoFar = Integer.MIN_VALUE;
    maxDiff = 0;
    for (int i = prices.length - 1; i >= 0; i--) {
        maxSoFar = Math.max(maxSoFar, prices[i]);
        maxDiff = Math.max(maxDiff, maxSoFar - prices[i]);
        bestFrom[i] = maxDiff;
    }

    int maxTwoTrades = 0;
    for (int i = 0; i < prices.length; i++) {
        int maxSecondTrade = (i+1 < prices.length) ? bestFrom[i+1] : 0;
        maxTwoTrades = Math.max(maxTwoTrades, bestTill[i] + maxSecondTrase);
    }

    return maxTwoTrades;
}
```