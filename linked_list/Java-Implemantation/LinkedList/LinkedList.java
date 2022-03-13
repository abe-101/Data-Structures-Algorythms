package LinkedList;

public class LinkedList {
    Node head;
    Node tail;

    /*
    public LinkedList() {
        head = null;
        tail = null;
    }
*/
    // Getters and Setters
    public LinkedList(Node head, Node tail) {
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

        if (node == null) {
           throw new IndexOutOfBoundsException(
                        "No node at index " + Integer.toString(n));
        }
        return node;
    }

    public void append(Node toAdd) {
        if (head == null) {
            head = toAdd;
        } else {
            tail.setNext(toAdd);
        }
        tail = toAdd;
    }
}

