---
title: 8-Path-Exists
updated: 2022-03-09 04:16:20Z
created: 2022-03-08 20:14:35Z
tags:
  - backtracking
  - maze
  - medium
---

## 

**Level**: Medium  

Maze Problem: You are given a 2D array that represents a maze. It can have 2 values - 0 and 1.
1 represents a wall and 0 represents a path.

The objective is to reach the bottom right corner, i.e, A[A.length-1][A.length-1]. You start from A[0][0]. You can move in 4 directions - up, down, left and right. Find if a path exists to the bottom right of the maze.
For example, a path exists in the following maze:
0 1 1 1
0 1 1 1
0 0 0 0
1 1 1 0

Questions to Clarify:
Q. How do you want the output?  
A. Return true if a path exists.  

Q. Does it matter if the end is a path or a wall?  
A. It doesn't matter, the last element (A[A.length-1][A.length-1]) can be anything. You just have to get there.  

Q. What if the array is empty or null?  
A. Return false (no path exists).  

Q. What if the array has just one element, e.g, {0} or {1}.  
A. Return true, because we're already at the last element.  


## Solution

**Pseudocode**:
```
boolean pathExists(a, i, j, memo)
    if i,j is out of bounds or a wall
        return false
    if i,j is end of maze
        return true
    if memo[i][j] is VISTING or NO_PATH_FOUND
        return false

    set memo[i][j] to VISITING

    fimd 4 points around (i,j)
    for each point
        check if path exists. Return true if it does

    // If we get here, path doesn't exist
    set memo[i][j] to NO_PATH_FOUND
    return false
```

**Test Cases**:
Edge Cases: matrix is empty or null, single element (1 & 0)  
Base Cases: matrix with 1 row/column  
Regular Cases: matrix with all walls, matrix with no walls, matrix with/without path to end, square matrix, rectangular matrix

Time Complexity: O(4^n) without memoization, O(n) with memoization, where n is the number of
elements in the matrix.

Space Complexity:  O(n) on both the memo and the recursion stack. Here, n is the number of elements in the matrix

**code:**
```java
public static boolean pathExists(int[][] a) {
    if (a == null || a.length == 0)
        return false;

    State[][] memo = new State[a.length][a[0].length];

    for (State[] states: memo)
        Arrays.fill(states, State.UNVISITED);

    return pathExists(a, 0, 0, memo);
}

public static boolean pathExists (int[][] a, int i, int j, State[][] memo) {
    if (oob(a, i, j) || a[i][j] == 1)
        return false;

    if (i == a.length - 1 && j == a[0].length -1) // end of maze
        return true;

    if (memo[i][j] == State.NO_PATH_FOUND || memo[i][j] == State.VISITING)
        return false;
    memo[i][j] = State.VISITING;

    Pair[] points = {
        new Pair(i+1,j),
        new Pair(i-1,j),
        new Pair(i, j+1),
        new Pair(i, j-1)
    };

    for (Pair point: points) {
        if (pathExists(a, point.getFirst(), point.getSecond(), memo)) {
            return true;
        }
    }

    memo[i][j] = State.NO_PATH_FOUND;
    return false;
}

// Helper code
public enum State {
    UNVISITED,
    VISITING,
    NO_PATH_FOUND;
}

private static boolean oob(int[][] a, int i, int j) {
    return i < 0 || i >= a.length || j < 0 || j >= a[0].length;
}

```

