---
title: 9-Sedoku
updated: 2022-03-09 15:35:57Z
created: 2022-03-09 15:20:46Z
---

## Sedoku

**Level**: Medium

Sudoku Solver: Given a Sudoku board, find a solution. The board can have some squares filled
out already. You have to fill the rest of the squares.
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
We use backtracking here. we try placing all 9 numbers int the box. we only place a number if it doesn't violate the rules. If we reach the end we have found a solution.
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
            place candidate in checher
            board[i][j] = candidate
            
            if solveSedoku(boead, next_i, next_j, checker)
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
