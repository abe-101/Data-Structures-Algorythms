---
title: 6-Evaluate-With-parenthesis
updated: 2022-03-23 22:01:07Z
created: 2022-03-23 21:56:36Z
---

## **Evaluate With Parenthesis**

<ins>**Level**: Hard</ins>
Given an arithmetic expression with *,/,- & + operators and single digit numbers,
evaluate it and return the result.
The expression can also contain parenthesis.
For example,
1 + 2 / 1 + 3 * 2 ==> 9
1 + (1 + 3) * 2 ==> 9
1 + 2 / (1 + 3) * 2 ⇒ 1

## Solution

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
        } else if (ch == '(') {
            operator.push(ch);
        } else if (ch == ')') {
            process(operator, operand);
        }
        operator.pop();
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
        case '(':
        case ')': return 0;
        default: throw new IllegalArgumentException("Invalid operator: " ch);
    }
}

private static void process(Stack<Character> operator, Stack<Integer> operand) {
    int num2 = operand.pop()
    int num1 = operand.pop()

    char op = operator.pop();

    int result = 0;

    while(op) {
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
