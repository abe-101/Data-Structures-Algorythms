---
title: 9-Sedoku
updated: 2022-03-11 17:15:20Z
created: 2022-03-09 15:20:46Z
tags:
  - backtracking
  - medium
  - sudoku
---

## Sedoku

**Level**: Medium

Sudoku Solver: Given a Sudoku board, find a solution. The board can have some squares filled out already. You have to fill the rest of the squares.
(Rules of Sudoku are as follows: In each column, row and 3 x 3 square, you cannot
have duplicate numbers. Also, only numbers 1-9 are allowed.)

Questions to Clarify:
Q. How is the input presented?
A. You're given a 2D array that represents the board. Each empty square has a value of 0.

Q. Will the board be of a fixed size?
A. Yes, the board will always be 9X9.

Q. How do you want the output?
A. Fill up the board with a valid answer.

Q. What if there is no solution. What do we return?
A. You can throw an error if no solution is found, i.e, the board is invalid.

## Solution

We use backtracking here. We try placing all 9 numbers int the box. we only place a number if it doesn't violate the rules. If we reach the end we have found a solution.
How do we check if it follows the rules? We could use the brute force way and go through each row, colom and box.
A better approach is to maintain an index. We keep a boolean matrix that keeps track of numbers in each row, another to keep track for columns and 3x3 boxes.
**Pseudocode**:

```
solveSedoku(board, i j, checker)
    if i == board.length
        return true // we found an answer
    
    if board[i][j] is provided // recurse to the next index
        return solveSekodu(board, next_i, next_j, checker)
    
    for candidates 1 to 9 {
        if (candidate can be placed) {
            place candidate in checker
            board[i][j] = candidate
            
            if solveSedoku(board, next_i, next_j, checker)
                return true
    
            remove candidate from checker
            board[i][j] = 0
        }
    }
    // no solution found
    return false
```

**Test Cases**:
Edge Cases: empty board, invalid board (no solution possible)
Base Cases: board with 1 element provided
Regular Cases: normal board with many elements provided

Time Complexity: O(9n), where n is the number of squares on the board.
Space Complexity: O(n), where n is the number of squares on the board.

**code:**
```
class solveSudokuDemo {
    public static void solveSudoku(int[][] board) {
        BoardChecker checker = new BoardChecker(board);

        boolean success = solveSudoku(board, 0, 0, checker);
        if (!success) {
            throw new IllegalArgumentException("Board has no solution");
        }
    }

    public static boolean solveSudoku(int[][] board, int i, int j, BoardChecker checker) {
        if (i == board.length)
            return true;

        Pair next = nextSquare(i, j);

        if (board[i][j] != 0)
            return solveSudoku(board, next.i(), next.j(), checker);

        for (int candidate = 1; candidate <= 9; candidate++) {
            if (checker.canPlace(i, j, candidate)) {

                // place candidate on sqaure
                checker.place(i, j, candidate);
                board[i][j] = candidate;

                if (solveSudoku(board, next.i(), next.j(), checker))
                    return true;

                // remove candidate from sqaure
                checker.remove(i, j, candidate);
                board[i][j] = 0;
            }
        }

        // no solution found
        return false;
    }

    // Helper code
    public static Pair nextSquare(int i, int j) {
        if (j == 8)
            return new Pair(i + 1, 0);
        else
            return new Pair(i, j + 1);
    }
    public static class BoardChecker {

        boolean[][] row = new boolean[9][10];
        boolean[][] column = new boolean[9][10];
        boolean[][] box = new boolean[9][10];

        public BoardChecker(int[][] board) {
            // add existing numbers to checker
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    if (board[i][j] != 0) {
                        place(i, j, board[i][j]);
                    }
                }
            }
        }

        public boolean canPlace(int i, int j, int number) {
            if (row[i][number])
                return false;

            if(column[j][number])
                return false;

            if (box[boxNumber(i,j)][number])
                return false;

            return true;
        }

        public boolean place(int i, int j, int number) {
            if(!canPlace(i, j, number))
                return false;

            row[i][number] = true;
            column[j][number] = true;
            box[boxNumber(i,j)][number] = true;

            return true;
        }

        public void remove(int i, int j, int number) {
            row[i][number] = false;
            column[j][number] = false;
            box[boxNumber(i,j)][number] = false;
        }

        public int boxNumber(int i, int j) {
            return (i/3)*3 + (j/3);
        }
    }

    public static class Pair {
        int i;
        int j;

        public Pair(int i, int j) {
            this.i = i;
            this.j = j;
        }

        public int i() {
            return i;
        }

        public int j() {
            return j;
        }
    }
}
```