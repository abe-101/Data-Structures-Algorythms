class printSubsetsDemo {
    public static void printSubsets(int[] a) {
        if (a == null || a.length == 0)
            return;
    
        int[] buffer = new int[a.length];
        printSubsetsHelper(a, buffer, 0, 0);
    }
    
    public static void printSubsetsHelper(int[] a, int[] buffer, int startIndex,
            int bufferIndex) {
          for (int i = 0; i < bufferIndex; i++) {
         		System.out.print(buffer[i]);
        }
        System.out.println();
        
        // termination cases - buffer full
        if (bufferIndex == buffer.length) {
            return;
        }
        if (startIndex == a.length) {
            return;
        }
    
        // find candidates that go into current buffer index
        for (int i = startIndex; i < a.length; i++) {
            // place item into buffer
            buffer[bufferIndex] = a[i];
    
            // recurse to next buffer index
            printSubsetsHelper(a, buffer, i + 1, bufferIndex + 1);
        }
    }
    public static void main(String[] args) {
        int arr[] = {1, 2, 3};
        printSubsets(arr);
    }
}
