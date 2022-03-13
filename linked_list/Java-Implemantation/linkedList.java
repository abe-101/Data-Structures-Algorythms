public class Node {
    Node next;
    int data;

    // Getters and Setters
    public Node(Node next, int data) {
        super();
        this.next = next;
        this.data = data;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }

    public int getData() {
        return data;
    }

    public void setData(int data) {
        this.data = data;
    }
}

public class LinkedList {
    Node head;
    Node tail;

    // Getters and Setters
    publicLinkedList(Node head, Node tail) {
        super();
        this.head = head;
        this.tail = tail;
    }

    public Node getHead() {
        return head;
    }

    public void setHead(Node head) {
        this.head = head;
    }

    public Node getTail() {
        return tail;
    }

    public void setTail(Node tail) {
        this.tail = tail;
    }

    /*
     * Get the nth element of the list.
     * Note: Here, the forst node is 1. It's not the zerp based like
     *       in an array
     */
    public Node get(int n) {
        Node node = head;
        for (int i = 0; i < n-1; i++) { // move forward n-1 times
            if (node != null) {
                node = node.getNext();
            } else {
                throw new IndexOutOfBoundsException(
                        "No node at index " + Integer.toString(n));
            }
        }

        return node;
    }
}
