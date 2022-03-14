import LinkedList.*;
import javafx.util.Pair;

class LinkedListDemo {
    public static void main(String[] args) {
        Node n = new Node(null, -1);
        LinkedList l = new LinkedList(n, n);
        for (int i = 0; i < 9; i++) {
            n = new Node(null, i);
            l.append(n);
        }
        Node node = new Node(null, -1);
        for (int i = 1; i < 10; i++) {
            node = l.get(i);
            int data = node.getData();
            System.out.println(data);
        }
        LinkedList odd = new LinkedList();
        LinkedList even = new LinkedList();

    }
}

