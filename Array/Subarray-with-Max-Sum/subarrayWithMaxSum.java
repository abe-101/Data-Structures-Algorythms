public static Integer subarrayWithMaxSum(int[] a) {
    if (a == null || a.length == 0)
        throw new IllegalArgumentException("Input array is empty or null");

    int result = a[0], maxEndingHere= a[0];

    for (int i = 1; i < a.length; i++) {
        maxEndingHere = Math.max(maxEndingHere + a[i], a[i]);
        result = Math.max(result, maxEndingHere);
    }
    return result;
}
