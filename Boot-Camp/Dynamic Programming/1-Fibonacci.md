---
title: 1-Fibonacci
updated: 2022-03-30 14:15:26Z
created: 2022-03-30 14:00:48Z
tags:
  - dp
  - fibonacci
---

## **Fibonacci**

Fibonacci Numbers Solution without Dynamic Programming (just Recursion)
```java
public int fibonacci(int n) {
    if (n == 1 || n == 0)
        return 1;

    return fibonacci(n-1 + fibonacci(n-2);
}
```

Fibonacci Numbers Solution with Dynamic Programming (Recursion + Memoization)
```java
public int fibonacciWithMemo(int n, HashMap<Integer, Integer> map) {
    if (n == 1 || n == 0)
        return 1;
    if(map.containKey(n)) // lookup memo
        return map.get(n);

    int result = fibonacciWithMemo(n-1, map) + fibonacciWithMemo(n-2, map);
    map.put(n, result;  insert memo
    return result;
}
```

Fibonacci Numbers Solution with Dynamic Programming (Tabulation)
Note​: In this problem, we just need the last two values, so we only save 2 values at a time.
```java
public static int fibonacci(int n) {
    if (n < 1)
        throw new IllegalArgumentException();

    int nMinus1 = 1, nMinus2 = 1, nth = 1;
    for (int i = 3; i <= n; i++) {
        nth = nMinus1 + nMinus2;

        // update n-1 and n-2
        nMinus2 = nMiinus1;
        nMinus1 = nth;
    }
    return nth;
}
```
