---
title: 11-Find-Cycle-Start
updated: 2022-03-15 15:36:47Z
created: 2022-03-15 15:12:34Z
---

## **Find Cycle Start**

<ins>**Level**: Medium</ins>

Given a Linked List with a cycle, find the node where the cycle begins.

Questions to Clarify:
Q. Can the entire list be a cycle?  
A. Yes  

## Solution
first we detect a cycle, then find the length of the cycle.
Once you know the length of the cycle, it makes things easier. Let's say the length is L.
Simply take 2 pointers ​A​ and ​B​, both at the start of the list. Move​ A​ forward by the L nodes.
Now, advance both pointers by 1 until they meet. The node at which they meet will be the start of the
cycle.
Why does this work? Once you've found the length of the cycle (N nodes), then if 2 pointers are N
nodes apart, they will eventually meet at the start when you move them forward together.

**Pseudocode**:
```
advance fast and slow pointers until they meat
find the length of the cycle, by advancing one of the
pointers around the cycle
Once you know the length L move both pointers to the head of list
advance one of the pointers by L
now keep advancing both pointers by 1 node, until they meet.
the node they meet is the starting point of the cycle
```

<ins>Test Cases:</ins>
Edge Cases: no node in list  
Base Cases: single element cycle  
Regular Cases: cycle starts in middle, entire list is a cycle  

Time Complexity: O(n)  
Space Complexity: O(1)  

**code:**
```
public static int findCycleStart(Node head) {
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
        return null;

    fast = fast.getNext();
    int cycleNodes = 1;
    while (fast != slow) {
        fast = fast.getNext();
        cycleNodes += 1;
    }

    // find start of cycle
    Node front = head, back = head;
    For(int i = 0; i < cycleNodes; i++) {
        front = front.getNext();
    }
    while (front != back) {
        front = front.getNext();
        back = back.getNext();
    }

    return front;
}        
```
