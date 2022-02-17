public static Pair<Integer> shortestUnsortedSubarray(int[] a) {
    if (a == null || a.length == 0)
        return null;

    int start, end;

    // find dip
    for (start = 0; start < a.length - 1; start++) {
        if (a[start + 1] < a[start])
            break;
    }

    // no dip found, array is already sorted
    if (start == (a.length - 1))
        return null;

    // find bump
    for (end = a.length - 1; end > 0; end--) {
        if (a[end - 1] > a[end])
            break;
    }

    // find min and max of a[start..end]
    int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
    for (int k = start; k <= end; k++) {
        if (a[k] > max)
            max = a[k];

        if (a[k] < min)
            min = a[k];
    }

    // expand start and end outward
    while (start > 0 && a[start -1] > min) {
        start--;
    }
    while (end < (a.length -1) && a[end + 1] < max) {
        end++;
    }

    return new Pair<Integer>(start, end);
}
