---
title: 4-Stack-with-Max
updated: 2022-03-23 17:08:57Z
created: 2022-03-23 16:07:57Z
---

## **Stack With Max**

<ins>**Level**:</ins>

Questions to Clarify:  
Q. Can I use extra space apart from the stack data?   
A. Yes, you can use extra space.  

Q. What to return if the stack is empty?  
A. Throw an exception.  

## Solution

<ins>Solution #1:</ins>

Store the max as a pair with each element  

```
insert(A)
    max = Maximun of A and the current max
    push(Pair<A,max>)

max()
    return the max on the top of the stack

pop()
    pop the pair on top, return value
```

<ins>Solution #2:</ins>
Every time you encounter a new max store it in a seperate max stack.

This implementation is a bit more space efficient because we don't
store a new value until a new max is found. It has the same space
complexity though - O(n).

**Pseudocode**:

```
main-stack
max-stack

insert(A)
    if A is >= max-stack()
        max-stack.push(A)
    main-stack.push(A)

max()
    max-stack.top()

pop()
    popped-value = main-stack.pop()
    if popped-value == max
        max-stack.pop()
```

<ins>Test Cases:</ins>
Edge Cases: Empty stack  
Base Cases: Stack with 1 value  
Regular Cases: insert smaller value, insert equal to max, insert larger value  

Time Complexity: ​O(1) for push and pop  
Space Complexity:​ O(n) for n insertions  

**code:**

```java
public class StackWithMax {
    Stack<Integer> main;
    Stack<Integer> max;

    public StackWithMax() {
        main = new Stack<>();
        max = new Stack<>();
    }

    public void push (int a) {
        main.push(a);
        if (max.isEmpty(() || a >= max.peek())
            max.push(a);
    }

    public int max() throws EmptyStackException {
        if (max.isEmpty())
            throw new EmtpyStackException();
        return max.peek();
    }

    public int pop() throws EmptyStackException {
        if (max.isEmpty())
            throw new EmtpyStackException();
        int item = main.pop();
        if (max.peek() == item)
            max.pop();
        return item;
    }
}
```