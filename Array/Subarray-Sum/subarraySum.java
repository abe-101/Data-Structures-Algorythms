public static Pair<Integer> subarray(int[] a, int target) {
    if (a == null || a.length == 0)
        return null;

    int start = 0, end = 0, sum = a[0];
    
    while (start < a.legnth) {
        if (start > end) {
            end = start;
            sum = a[start];
        }

        if (sum < target) {
            if (end + 1 == a.length)
                break;
            end++;
            sum = sum + a[end];
        } else if (sum > target) {
            sum = sum - a[start];
            start++;
        } else {
            return new Pair<Integer>(start, end);
        }
    }

    return null;
}

