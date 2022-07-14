---
title: 0700-Search in a Binary Search Tree
updated: 2022-07-14 15:12:36Z
created: 2022-07-14 15:11:51Z
source: https://leetcode.com/problems/search-in-a-binary-search-tree/
---

700\. Search in a Binary Search Tree

Easy

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

**Example 1:**

![](../_resources/tree1_d670ad783521401c99dc967f144edbe8.jpg)

```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

```

**Example 2:**

![](../_resources/tree2_3ebffb34e9fa4edc9a769dd29572cf05.jpg)

```
Input: root = [4,2,7,1,3], val = 5
Output: []

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 5000]`.
- `1 <= Node.val <= 10<sup>7</sup>`
- `root` is a binary search tree.
- `1 <= val <= 10<sup>7</sup>`

**Solution:**
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
```
Time Complexity: O(log n)
Space Complexity: O(log n)