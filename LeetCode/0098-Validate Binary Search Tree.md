---
title: 0098-Validate Binary Search Tree
updated: 2022-07-14 15:51:17Z
created: 2022-07-14 15:50:20Z
source: https://leetcode.com/problems/validate-binary-search-tree/
---

98\. Validate Binary Search Tree

Medium

Given the `root` of a binary tree, *determine if it is a valid binary search tree (BST)*.

A **valid BST** is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

![](../_resources/tree1_97541037f96d479c8ebe66eaa1c75967.jpg)

```
Input: root = [2,1,3]
Output: true

```

**Example 2:**

![](../_resources/tree2_b1371869afa54385a4eb0e9c3af45849.jpg)

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 10<sup>4</sup>]`.
- `-2<sup>31</sup> <= Node.val <= 2<sup>31</sup> - 1`

**Solution:**
```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.in_order_traversal(root, values)
        for i in range(1, len(values)):
            if values[i-1] >= values[i]:
                return False
        return True
    
    def in_order_traversal(self, root, values):
        if root is None:
                return
        self.in_order_traversal(root.left, values)
        values.append(root.val)
        self.in_order_traversal(root.right, values)
```
Time Complexity: O(n)
Space Complexity: O(n)