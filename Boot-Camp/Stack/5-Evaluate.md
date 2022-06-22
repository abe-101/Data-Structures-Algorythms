---
title: 5-Evaluate
updated: 2022-05-10 16:08:38Z
created: 2022-03-23 21:06:13Z
---

## **Evaluate**

<ins>**Level**: Hard</ins>
Given an arithmetic expression with *,/,- & + operators and single digit numbers evaluate it and return the result.  
For example,  
1 + 2 / 1 + 3 * 2 ==> 9

Questions to Clarify:  
Q. Can the expression have parentheses - '()'?  
A. No, it will only have those 4 operators of single digit numbers.

Q. Can we assume the input to be an array of characters?   
e.g, \['1','+','2','','1'..\]  
A. Yes that’s fine.

Q. When we divide two numbers, is the result an integer or can it be a fraction?  
E.g, 1⁄2 is 0 or 0.5?  
A. Depends on your language. Here, we will use integer arithmetic, so 1⁄2 will be 0.

Q. Can we assume that the expression is valid?  
A. Yes, assume that the expression is valid.

Q. If the expression is empty, can I return 0?  
A. Yes.

## Solution

**Pseudocode**:

```
// Helper function might not have to implement
process() function - evaluates the operator on top of the operator stack and
                     pushes the result onto the operand stack.

precedence() funcrion - returns the precedence of an operator

Main function
init operant, operator stack
loop through character ch in expression
    if ch is operand
        push into operand stack
    if ch is operator
        while precedence(top of operator stack) >= precedence(ch)
            run process() function to evaluate the top operator
        push ch to operator stack

while operator stack is not empty
    run process() function

At the end result should be the only number on the operand stack
```

<ins>Test Cases:</ins>
Edge Cases: Empty expression, single number in expression  
Base Cases: Single operation (​1+2, 1*2​)  
Regular Cases: Multiple operators

Time Complexity: O(n)  
Space Complexity: O(n) because we store a copy of the operator/operands in the stacks

**code:**

```java
public static int evaluate(char[] expression) {
    if (expression == null || expression.length == 0)
        return 0;

    Stack<Integer> operand = new Stack<>();
    Stack<Character> operand = new Stack<>();
    for (char ch : expression) {
        if (isOperand(ch)) {
            operand.push(ch-'0');
        else if (isOperator(ch)) {
            while (!operator.isEmpty()
                    && precedence(operator.peek()) >= precedence(ch)) {
                proccess(operator, operand);
            }
            operator.push(ch);
        }
    }

    while (!operator.isEmpty() {
        proccess(operator, operand);
    }

//helper function
private static boolean isOperand(char ch) {
    return (ch >= '0') && (ch <= '9');
}

private static boolean isOperator(char ch) {
    return (ch == '+') || (ch == '-') || (ch == '*') || (ch == '/') 
}

private static int precedence(char ch) {
    switch(ch) {
        case '/':
        case '*': return 2;
        case '+':
        case '-': return 1;
        default: throw new IllegalArgumentException("Invalid operator: " ch);
    }
}

private static void process(Stack<Character> operator, Stack<Integer> operand) {
    int num2 = operand.pop()
    int num1 = operand.pop()

    char op = operator.pop();

    int result = 0;

    swich(op) {
        case '/': result = num1 / num2;
            break;
        case '*': result = num1 * num2;
            break;
        case '+': result = num1 + num2;
            break;
        case '-': result = num1 - num2;
            break;
    }
    operand.push(result);
```