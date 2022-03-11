import java.util.HashMap;

class fibonacciDemo {
    public static int fibonacci(int n) {
        return fibonacci(n, new HashMap<Integer, Integer>());
    }
    
    public static int fibonacci(int n, HashMap<Integer, Integer> memo) {
        if (n == 1 || n == 2)
            return 1;
        if (memo.containsKey(n))
            return memo.get(n);
    
        int result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
        memo.put(n, result);
        return result;
    }

    public static void main(String[] args) {
        System.out.println(fibonacci(9));
    }
}
