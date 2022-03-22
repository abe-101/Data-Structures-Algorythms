---
title: 12-LRU-Cache
updated: 2022-03-22 14:52:25Z
created: 2022-03-16 13:08:42Z
---

## **LRU Cache**
Implement a data structure for a Least Recently Used (LRU) cache.

<ins>**Level**:Hard</ins>

Questions to Clarify:
Q. What should we return if an entry wasn't found?
A. Return null

## Solution

**Pseudocode**:
```
write(key, value)
    if full:
        remove LRU Node
    add Node to front

read(key)
    remove Node
    add Node back to the front
    return node's value
```
<ins>Test Cases:</ins>
Edge Cases: Null Node, Empty Data structure  
Base Cases: Single element in Linked Hash Table  
Regular Cases: Read/Write, Cache Full/Empty/Not Full  

Time Complexity: O(1) for both reads and writes  
Space Complexity: O(n) where n is the amount of data in cache  


**code:**
```
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
public class Node<K,V> {
    Node<K,V> next;
    Node<K,V> past;
    K key;
    V value;


    public Node(K key, V value) {
        super();
        this.key = key;
        this.value = value;
    }


    public Node<K,V> getNext() {
        return next;
    }

    public void setNext(Node<K,V> next) {
        this.next = next;
    }

    
    public Node<K,V> getPrev() {
        return prev;
    }


    public void setPrev(Node<K,V> prev) {
        this.prev = prev;
    }


    public K getKey() {
        return key;
    }


    public V getValue() {
        return value;
    }
}

