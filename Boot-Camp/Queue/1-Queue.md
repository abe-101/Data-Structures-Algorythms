---
title: 1-Queue
updated: 2022-03-27 17:56:58Z
created: 2022-03-27 17:33:47Z
tags:
  - easy
  - queue
---

## **Queue**

<ins>**Level**: Easy</ins>

Questions to Clarify:
Q. Is the size of the array fixed?
A. Yes, the array has a fixed size provided as an input.
Q. Can we assume that the Queue will store integers?
A. Yes

## Solution

Implement a circular queue in the array. Maintain 2 pointers in the array, front and back. Add elements to the back and remove elements from the front.
**The trink to making it easy: maintain a length variable* This keeps the number of elements in the queue. This way, we can easily tell if the queue is full or empty.

**Pseudocode**:

```
front = 0
back = 0
length = 0
add()
    if (length == a.length)
        throw exception
    a[back] = n
    back = (back+1) % a.length
    length++

remove()
    if (length == 0)
        throw empty queue exception
    result = a[front]
    front = (front+1) % a.length
    length--
    return result

```

<ins>Test Cases:</ins>
Edge Cases: Empty array, empty queue
Base Cases: Single element in queue, 2 elements in queue
Regular Cases: Queue full, general case

Time Complexity: O(1) for insertion and deletion
Space Complexity: O(1) extra space after the initial array

**code:**

```java
public class Queue {
    int[] a;

    int front;
    int back;
    int length;
    
 	public Queue(int capacity) {
        a = new int[capacity];
        front = back = length;
    }
    
    public void add(int item) throws QueueFullException {
        if (length == a.length)
            throw new QueueFullException();
        a[back] = item;
        back (back+1) % a.length;
        length++;
    }
    
    public int remove() throws QueueEmptyException {
        if (length == 0)
            throw new QueueEmptyException();
        int result = a[front];
        front (front+1) % a.length;
        length--;
        return result;
    }
}
```