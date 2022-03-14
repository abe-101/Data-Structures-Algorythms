---
title: 2-Appennd-Function
updated: 2022-03-13 21:22:21Z
created: 2022-03-13 21:17:32Z
---

## Append Function

**Level**: Easy  
The append function is especially useful in Linked List problems. On the face, it is
pretty simple. But once you know it by heart, you can apply it to a ton of problems quickly.
To Implement​: A function that adds a node to a linked list.


**Pseudocode**:
```
append(Node n)
    if head is null (list empty)
        n is new head
        n is new tail
    else
        add n to tail
        n is new tail
```

Time Complexity: O(1) since we know the tail  
Space Complexity: O(1)  

**code:**
```
public class LinkedList {
    Node head;
    Node tail;

    public LinkedList() {
        head = null;
        tail = null;
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
```

