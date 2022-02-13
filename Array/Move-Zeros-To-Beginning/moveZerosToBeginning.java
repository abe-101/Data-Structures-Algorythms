public static void moveZerosToBeginning(int[] a) {
    int boundry = 0;

    for (int i: a) {
        if (a[i] == 0) {
            Utils.swap(a, i, boundary);
            boundary += 1;
        }
    }
}
