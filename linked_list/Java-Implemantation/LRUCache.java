public class LRUCache<k, V> {
    // map keys to node
    HashMap<K, Node<K, v>> map;


    // Linked list variables
    Node<K,V> head;
    Node<K,V> tail;

    // Maximum nodes the cache can hold.
    int capacity;

    public LRUCache(int capacity) {
        this.map = new HashMap<>();
        this.capacity = capacity;
    }

    // Read a value from cache.
    public V read(K key) {
        Node<K,V> node = map.get(key);
        if(node == null)
            return null;

        remove(key); // remove from linked hash table
        add(node.getKey(), node.getValue()); // add back to front
        return node.getValue();
    }

    // Write a value to cache
    public void write(K key, V value) {
        if (map.size() == capacity) { // cache is full, remove the head
            remove(head.getKey());
        }

        add(key, value);
    }

    // Remove a node from the linked hash table
    public void remove(K key) {
        if(!map.containsKey(key))
            return;
        Node<K,V> toRemove = map.get(key);
        removeFromLinkedList(toRemove);
        map.remove(key);
    }

    // Add a node to the end of the Linked Hash Table
    private void add(K key, V value) {
        Node<K,V> newNode = new Node<>(key, value);
        appendToLinkedList(newNode);
        map.put(key, newNode);
    }

    // Helper Functions
    //
    // Append Function for a doubly linked list.
    public void appendToLinkedList(Node<K,V> toAdd) {
        if (head == null){
            head = toAdd;
        } else {
            tail.setNext(toAdd);
            toAdd.setPrev(tail);
        }
        tail = toAdd;
    }

    // Remove a Node from a doubly linked list
    public void removeFromLinkedList(Node<K,V> toRemove) {
        if (toRemove.getPrev() != null)
            toRemove.getPrev().setNext(toRemove.getNext());
        if (toRemove.getNext() != null)
            toRemove.getNext().setPrev(toRemove.getPrev());

        if (toRemove == head)
            head = toRemove.getNext();

        if (toRemove == tail)
            tail = toRemove.getPrev();
    }
}

// Node that stores Key and values. It is a doubly linked list
// so it stores next and previous nodes.
//
