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
    public static void printBoard(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 0)
                    System.out.print("* ");
                else
                    System.out.print(board[i][j] + " ");
                if (j == 2 || j == 5) {
                    System.out.print(" ");
                }
            }
            System.out.println();
            if (i == 2 || i ==5) {
                System.out.println();
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {

        int[][] board = {{ 8, 0, 0, 0, 0, 0, 0, 0, 0 },
                         { 0, 0, 3, 6, 0, 0, 0, 0, 0 },
                         { 0, 7, 0, 0, 9, 0, 2, 0, 0 },
                         { 0, 5, 0, 0, 0, 7, 0, 0, 0 },
                         { 0, 0, 0, 0, 4, 5, 7, 0, 0 },
                         { 0, 0, 0, 1, 0, 0, 0, 3, 0 },
                         { 0, 0, 1, 0, 0, 0, 0, 6, 8 },
                         { 0, 0, 8, 5, 0, 0, 0, 1, 0 },
                         { 0, 9, 0, 0, 0, 0, 4, 0, 0 }};
        printBoard(board);
        solveSudoku(board);
        System.out.println("\n******Solution******\n");
        printBoard(board);
    }
}


