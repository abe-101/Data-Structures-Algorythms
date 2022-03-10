---
title: 10-Word-Break
updated: 2022-03-10 18:42:47Z
created: 2022-03-10 17:36:36Z
---

## Word Break

**Level**: Medium

Word Break Problem: Given a String S, which contains letters and no spaces, determine if you
can break it into valid words. Return one such combination of words.
You can assume that you are provided a dictionary of English words.
For example:
S = "ilikemangotango"
Output:
Return any one of these:
"i like mango tango"
"i like man go tan go"
"i like mango tan go"
"i like man go tango"

Questions to Clarify:
Q. Can I return the result as a list of strings (each string is a word)?
A. Yes

Q. What to return if no result is found?
A. Just return null.

Q. What if there are multiple possible results?
A. Return any one valid result.

Q. What if the String is empty or null?
A. Return null.

## Solution

**Pseudocode**:

```
word_break(s, start, dict, list<string> result, memo)
    // base case
    if (start == s.length)
        return true

    // check memo
    if memo[start] is NOT_FOUND
        return false

    for i: start to a.length-1 {
        if s[start..i] is a valid word
            add s[start..i] to result
            // try recursing from i+1
            if word_break(s, i+1, dict, result, memo) returns true
                return true. result cantains the valid words
            else
                remove s[start..i] from results
                set memo[i+1] to NOT_FOUND, because there is no combo from i
    }

    return false // no result found
```

**Test Cases**:
Corner Case -
Base Case -
Regular Case -

Time Complexity:
Space Complexity:

**code:**

```
public static List<String> wordBreak(String s, HashSet<string> dictionary) {
    if (s == null || s.isEmpty())
        return null;

    State[] memo = new State[s.length()];
    Arrays.fill(memo, State.UNVISITED);

    List<String> result = new ArrayList<String>();

    if (wordBreak(s, 0, memo, result, dictionary)) {
        return result;
    }

    return null;
}

public static boolean wordBreak(String s, int start, state[] memo,
        List<String> result, HashSet<String> sictionary) {
    if (start == s.length())
        return true;

    if (memo[start] == State.NOT_FOUND)
        return false;

    for (int i = start; i < s.length(); i++) {
        String candidate = s.substring(start, i + 1);

        if (dictionary.contains(candidate)) {
            result.add(candidate);
            if (wordBreak(s, i + 1, memo, result, dictionary)) {
                return true;
            } else {
                result.remove(result.size() - 1); // remove candidate
                memo[i+1] = State.NOT_FOUND;
            }
        }
    }

    return false;
}

// Helper code
public emun State {
    UNVISITED;
    NOT_FOUND;
}
```