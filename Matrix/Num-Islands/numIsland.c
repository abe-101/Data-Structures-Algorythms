#include <stdio.h>

int HEIGHT;
int WIDTH;

void isIsland(char** grid, int row, int col){
    if(row>=WIDTH || col>=HEIGHT || row<0 || col<0){
        return;
    }
    
    if (grid[row][col] == '0') {
        return;
    }
    // mark spot visted
    grid[row][col] = '0';
    
    isIsland(grid, row + 1, col);
    isIsland(grid, row, col + 1);
    isIsland(grid, row - 1, col);
    isIsland(grid, row, col - 1);
}

int numIslands(char** grid, int gridSize, int *gridColSize){
    WIDTH = gridSize;
    HEIGHT = gridColSize[0];
    int count = 0;
    
    for (int row = 0; row < WIDTH; row++) {
        for (int col = 0; col < HEIGHT; col++) {
            if (grid[row][col] == '1') {
                isIsland(grid, row, col);
                count++;
            }
        }
    }
    return count;
}

