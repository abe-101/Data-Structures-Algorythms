class pathExistsDemo {
    public static boolean pathExists(int[][] a) {
        if (a == null || a.length == 0)
            return false;

        State[][] memo = new State[a.length][a[0].length];

        //for (State[] states: memo)
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[0].length; j++) {
                memo[i][j] = State.UNVISITED;
            }
        }
            //Arrays.fill(states, State.UNVISITED);

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
            if (pathExists(a, point.i(), point.j(), memo)) {
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

    public static void main(String[] args) {
        int[][] matrix1 = {{0,1,1,1},
                           {0,1,1,1},
                           {0,0,0,0},
                           {1,1,1,0}};

        if (pathExists(matrix1)) {
            System.out.println("Found path!");
        } else {
            System.out.println("No path!");
        }
    }
}
