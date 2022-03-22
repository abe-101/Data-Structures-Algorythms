---
title: 9-Find-Cycle-Length
updated: 2022-03-15 15:29:46Z
created: 2022-03-15 14:00:59Z
---

## **Find Cycle Length**

<ins>**Level**: Medium</ins>
Given a linked list that has a cycle, find the length of the cycle. The length is in number of nodes.

Questions to Clarify:
Q. How do you want the output
A. Return the number of nodes in the cycle

Q. Can we assume the input has a cycle?
A. No

## Solution

This problem is an extension of finding cycles.

Once the fast and slow pointer meet, we know that they point to a node in the cycle. now keep advancing the fast pointer till it makes a full circle. The number of nodes it passed is the length of the cycle.

**Pseudocode**:

```
Advance fast and slow pointers until they meet
fast = fast.next;
nodes_passed = 1;
while fast != slow
    fast = fast = fast.next
    nodes_passed++
return nodes_passed
```

<ins>Test Cases:</ins>
Edge Cases: No cycle
Base Cases: Cycle of 1 node, Cycle of 2 nodes, 3 Nodes
Regular Cases: Odd cycle, even cycle, whole list is cycle

Time Complexity: O(n)
Space Complexity: O(1)

**code:**

```
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
```