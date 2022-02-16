public static int[] cloneEvenNumbers(int[] a) {
    if (a == null || a.length == 0)
        return a;

    int end = a.length, i = getLastNUmber(a);
    while (i >=  0) {
        if (a[i] % 2 == 0) {
            a[--end] = a[i];
        }
        a[--end] = a[i];
        i--;
    }
    return a;
}

public static int getLastNumber(int[] a) {
    int i = a.length -1;
    while (i >= 0 && a[i] == -1) {
        i--;
    }
    return i;
}
