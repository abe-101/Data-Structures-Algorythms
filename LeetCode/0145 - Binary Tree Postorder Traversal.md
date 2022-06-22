---
title: 0145 - Binary Tree Postorder Traversal
updated: 2022-06-22 18:14:45Z
created: 2022-06-22 18:12:48Z
source: https://leetcode.com/problems/binary-tree-postorder-traversal/
tags:
  - binary tree
  - iterative
  - python
  - recursion
---

145\. Binary Tree Postorder Traversal

Easy

Given the `root` of a binary tree, return *the postorder traversal of its nodes' values*.

**Example 1:**

<img width="127" height="199" src="../_resources/pre1_974c6843bf904c6eb3407c15b6a77784.jpg"/>

```
Input: root = [1,null,2,3]
Output: [3,2,1]

```

**Example 2:**

```
Input: root = []
Output: []

```

**Example 3:**

```
Input: root = [1]
Output: [1]

```

**Constraints:**

- The number of the nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

**Solution:**
Recursive:
```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        self._postorderTraversal(root, result)
        return result

        
    def _postorderTraversal(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        self._postorderTraversal(root.left, result)
        self._postorderTraversal(root.right, result)
        result.append(root.val)

```

Iterative:
```python
from collections import deque
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = deque([])
        stack = [ root ]
        
        while stack:
            node = stack.pop()
            result.appendleft(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result
```