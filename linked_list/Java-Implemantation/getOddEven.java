Import LinkedList.*;

class getOddEven {
    Public Pair<LinkedList> getOddEven(LinkedList input) {
        LinkedList odd = new LinkedList();
        LinkedList even = new LinkedList();
    
        Node current = input.getHead();
        int index = 0;
        while (current != null) {
            index++;
            LinkedList destination = index % 2 == 0 ? even : odd;
            destination.append(current);
            current = current.getNext();
        }
    
        if (even.getTail() != null)
            even.getTail().setNext(null);
    
        if (odd.getTail() != null)
            odd.getTail().setNext(null);
    
        return new Pair<LinkedList>(odd, even);
    }
}
