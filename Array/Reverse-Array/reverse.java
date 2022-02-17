public static void reverse(int[] a ) {
    if (a== null)
        return;
    int start = 0, end = a.length-1;

    while (start < end) {
        Utils.swap(a, start++, end--)
    }

