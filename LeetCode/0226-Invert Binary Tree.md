---
title: 0226-Invert Binary Tree
updated: 2022-07-08 00:47:49Z
created: 2022-07-08 00:46:50Z
source: https://leetcode.com/problems/invert-binary-tree/
---

226\. Invert Binary Tree

Easy

Given the `root` of a binary tree, invert the tree, and return *its root*.

**Example 1:**

<img width="500" height="165" src="../_resources/invert1-tree_75808a52c71f42ebac0bfe469c5eb760.jpg"/>

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

```

**Example 2:**

<img width="500" height="120" src="../_resources/invert2-tree_fcd0c2c3e8564626ac0eca3e065251dd.jpg"/>

```
Input: root = [2,1,3]
Output: [2,3,1]

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def _invertTree(root):
            if root is None:
                return
            root.right, root.left = root.left, root.right
            _invertTree(root.right)
            _invertTree(root.left)
            
        _invertTree(root)
        return root
```
