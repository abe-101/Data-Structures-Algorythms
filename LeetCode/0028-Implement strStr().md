---
title: 0028-Implement strStr()
updated: 2022-06-13 18:02:05Z
created: 2022-06-13 17:55:41Z
source: https://leetcode.com/problems/implement-strstr/
tags:
  - easy
  - python
---

28\. Implement strStr()

Easy

Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf%28java.lang.String%29).

**Example 1:**

```
Input: haystack = "hello", needle = "ll"
Output: 2

```

**Example 2:**

```
Input: haystack = "aaaaa", needle = "bba"
Output: -1

```

**Constraints:**

- `1 <= haystack.length, needle.length <= 10<sup>4</sup>`
- `haystack` and `needle` consist of only lowercase English characters.

**Solution:**
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
```