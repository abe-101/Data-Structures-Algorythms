public static int[] sortedSquare(int[] a) {
    if (a == null)
        return null;

    int start = 0, end = a.length-1;

    int[] result = new int[a.length];
    int resultIndex = result.length-1;
    
    while (start <= end) {
        // add larger one to the end of reslut
        if (abs(a[start]) > abs(a[end])) {
            result[resultIndex--] = square(a[start++]);
        } else {
            result[resultIndex--] = square(a[end--]);
        }
    }
    return result;
}


public static int abs(int number) {
    return number >= 0 ? number: -1 * number;
}


public static int square(int number) {
    return number * number;
}


