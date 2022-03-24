---
title: 1-Find
updated: 2022-03-23 14:56:32Z
created: 2022-03-22 18:30:46Z
tags:
  - easy
  - stack
---

## **Find**

<ins>**Level**: Easy</ins>

Find if a given number N exists in a stack S.

Questions to Clarify:  
Q. What output should I return?  
A. Return true if N is found, false otherwise.

Q. So I return true as soon as I find one instance of the number?  
A. Yes

## Solution

We travers through the stack with a temporary stack. when we find a node that is equal to N we return. Before returning we restore the original stack.

**Pseudocode**:

```
find(N, s)
    Stack temp = empty
    boolean found = false
    while s is not empty
        top = s.peek()
        if top == N
            found = true
            break
        temp.push(s.pop())
    
    while temp is not empty
        s.push(temp.pop())

    return found
```

<ins>Test Cases:</ins>
Edge Cases: empty stack, null stack  
Base Cases: one item in stack, 2 items in stack (N found/not-found)  
Regular Cases: many items in stack (N found/not-found)

Time Complexity: O(n)  
Space Complexity: O(1)

**code:**

```java
public static boolean find(int target, Stack<Integer> s) {
    if (s == null)
        return false;

    Stack<Integer> temp = new Stack<>();
    boolean found = false;
    
    while (!s.isEmpty()) {
        if (s.peek() == target) {
            found = true;
            break;
        }

    while (!temp.isEmpty()) {
        s.push(temp.pop());
    }

    return found;
}
```