---
title: 0125-Valid Palindrome
updated: 2022-07-10 19:35:04Z
created: 2022-07-07 19:09:44Z
source: https://leetcode.com/problems/valid-palindrome/
tags:
  - easy
  - palindrome
  - python
---

125\. Valid Palindrome

Easy

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

**Example 3:**

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

**Constraints:**

- `1 <= s.length <= 2 * 10<sup>5</sup>`
- `s` consists only of printable ASCII characters.

**Solution:**

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        s = "".join(s.split())
        s = s.lower()
        return s == s[::-1]
```

Time Complexity:O(n),
Space Complexity:O(n)


```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9"))
```