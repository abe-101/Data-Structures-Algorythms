---
title: 1-Implementation
updated: 2022-03-16 13:10:39Z
created: 2022-03-09 02:35:13Z
tags:
  - easy
  - linked list
---

* * *

## title: readme-template
updated: 2022-03-02 16:30:17Z
created: 2022-02-22 20:12:07Z

## Implementation

Implement a Linked List
**Level**: Easy

Questions to Clarify:
Q. Do you want a singly linked list or a doubly linked list?
A. Singly

**code:**

```
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

```