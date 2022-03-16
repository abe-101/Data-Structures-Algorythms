public static int findCycleLength(Node head) {
    Node fast = head, slow = head;
    while (fast != null) {
        fast = fast.getNext();
        if (fast == slow)
            break;
        if (fast != null) {
            fast = fast.getNext();
            if (fast == slow)
                break;
        }
        slow = slow.getNext();
    }

    if (fast == null) // no cycle found
        return -1;

    fast = fast.getNext();
    int nodesPassed = 1;
    while (fast != slow) {
        fast = fast.getNext();
        nodesPassed += 1;
    }
    return nodesPassed;
}
