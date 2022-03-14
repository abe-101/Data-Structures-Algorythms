---
title: 3-Sorted-LinkedList
updated: 2022-03-14 14:52:25Z
created: 2022-03-13 21:31:28Z
---

## Sorted LinkedList

**Level**: Easy

You are given a Linked List with nodes that have values 0, 1 or 2. Sort the linked list.

Questions to Clarify:
Q. Do I need to sort in place?
A. No, I want you to rearrange the existing nodes.

Q. How do you want the output?
A. Return the Head and Tail as a pair.

**Solution:**
We initialize 3 new linked lists for each value (0,1,2).
Then, we go through the list and use the append function to place each node in the
appropriate list.
After that, we simply join the 3 lists (0 -> 1 -> 2). This is the output.

**Pseudocode**:

```
init 3 lists
loop through input list
    apend node to appropriate list
combine 3 list using append function
```

Test Cases:
Edge Cases: empty list, null elements, invalid value
Base Cases: one node, 2 nodes
Regular Cases: all values present, one value only

Time Complexity: O(n)
Space Complexity: O(1)

**code:**

```
public static LinkedList sortList(LinkedList input) {
    if (input == null)
        return new LinkedList(); // empty list
    
    LinkedList list0 = new LinkedList();
    LinkedList list1 = new LinkedList();
    LinkedList list2 = new LinkedList();
    Node current = input.head();

    while(current != null) {
        Switch (current.getData()) {
            case 0: list0.append(current); break;
            case 1: list1.append(current); break;
            case 2: list2.append(current); break;
            default: throw new IllegalArgumentException(
                    "Invalid value: " + current.getData();
        }
        current = current.getNext();
    }
    
    // set tails to null
    if (list0.tail != null)
        list0.tail.next = null;
    
    if (list1.tail != null)
        list1.tail.next = null;
    
    if (list2.tail != null)
        list2.tail.next = null;
    
    // attach lists on sequence
    LinkedList result = new LinkedList();
    appendList(list0, result);
    appendList(list1, result);
    appendList(list2, result);

    return result;
}

void appendList (LinkedList toAppend, LinkedList original) {
    if (toAppend == null || toAppend.head == null)
        return;
    original.append(toAppend.head);
    original.tail = toAppend.tail;
}
```