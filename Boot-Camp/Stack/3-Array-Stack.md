---
title: 3-Array-Stack
updated: 2022-03-23 14:54:42Z
created: 2022-03-23 14:26:28Z
tags:
  - medium
  - stack
  - subarray
---

## **Array Stack**

<ins>**Level**: Medium</ins>

Use an array to implement 2 stacks.

Questions to Clarify:  
Q. Is the array of fixed size?  
A. Yes, the size is provided as input.  

Q. What to return if the array is full?  
A. Throw an exception.  

Q. We will implement push() and pop() functions of the stack, is there any other function you want?  
A. No, those two are enough.  

## Solution

We can use the 2 ends of the array as each stack. We keep adding elements at the 2 ends until they meet. At that point, we've run out of space.

**Pseudocode**:

```
a = new array[size]
int stack1 = 0, stack2 = a.length -1;
push(stack, item)
    if (stack1 > stack2 or stack1 >= a.length or stack2 < 0)
        array is full, throw exception
    a[stack] = item
    update stack value

pop(stack)
    if (stack is stack1 && stack1 == 0 or stack is stack2 && stack2 == a.length -1)
        stack is empty, throw exception
    result = a[stack]
    update stack value
    return result
```

<ins>Test Cases:</ins>
Edge Cases: Array empty, array full, ​s1​ empty/full, ​s2​ empty/full  
Base Cases: Single element in ​s1​/​s2​, array size 0,1,2  
Regular Cases: Array size 10  

Time Complexity: O(1) for both push() and pop()  
Space Complexity: ​O(1) - no extra space used apart from the array.  
However, if the interviewer wants to count the array in the space complexity, it will be O(n).

**code:**

```java
public class ArrayStack {
    int[] a;
    
    int s1;
    int s2;

    public class ArrayStack(int arraySize) {
        a = new int[arraySize];
        s1 = 0;
        s2 = a.length - 1;
    }
    
    public void push(int stackNumber, int item) throws StackFullException {
        if (stacknumber != 1 && stackNumber != 2)
            throw new IllegalArgumentException("Invalid stack number.");

        if (s1 > s2)
            throw new StackFullException();

        if (stackNumber == 1)
            a[s1++] = item;
        else
            a[s2--] = item;
    }

    public int pop(int stackNUmber throws StackEmptyException {
        if (stacknumber != 1 && stackNumber != 2)
            throw new IllegalArgumentException("Invalid stack number.");
        
        if (stackNumber == 1 && s1 > 0)
            return a[--s1];
        else if (stackNumber == 2 && s2 < a.length -1)
            return a[++s2]

        throw new StackEmptyException();
    }
}

public class StackFullException extends Exception {
    public StackFullException() {
    }
}

public class StackEmptyException extends Exception {
    public StackEmptyException() {
    }
}
```