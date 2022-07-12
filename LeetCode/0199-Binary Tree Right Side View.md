---
title: 0199-Binary Tree Right Side View
updated: 2022-07-11 21:10:51Z
created: 2022-07-11 21:09:45Z
source: https://leetcode.com/problems/binary-tree-right-side-view/
---

199\. Binary Tree Right Side View

Medium

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return *the values of the nodes you can see ordered from top to bottom*.

**Example 1:**

![](../_resources/tree_fed19809f6fa466f9aa1262417529530.jpg)

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

```

**Example 2:**

```
Input: root = [1,null,3]
Output: [1,3]

```

**Example 3:**

```
Input: root = []
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Solution:**
```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.traverse(root, 0, values)
        return values

    def traverse(self, root, levels, values):
        if root is None:
            return 
        if len(values) == levels:
            values.append(root.val)
    
        self.traverse(root.right, levels + 1, values)
        self.traverse(root.left, levels + 1, values)
```
Time Complexity: O(n)
Space Complexity: O(n)