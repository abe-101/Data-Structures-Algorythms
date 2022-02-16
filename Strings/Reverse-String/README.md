## Problem: Reverse the Words of a Sentence 

**Level**: easy

Given a sentence, reverse the words of the sentence.
For example,
"i live in a house" becomes "house a in live i"


Questions to Clarify:
Q. How to deal punctuation?
A. Assume there are no punctuations

Q. How to deal with capitalization (uppercase vs lowercase letters)?
A. Ignore the case, keep as it is.

Q. Can I allocate a new String for the result?
A. Yes, you can allocate a new String. Limit the space complexity to O(n).

## Solution
Strating from the end every time we find a space we add that word to the results.

**Pseudocode**:
```
result = empty string
current_word_end = str.length

i is str.length-1 to 0
    if str[i] is a space:
        extract str[i..ciurrent_word_ends], add it to result
        reset current_word_to_i
    extract first word str[0..ciurrent_word_ends] and to result
    
```
**Test Cases**:
Corner Cases: null string, empty string, single letter, single space, begins with space, ends with space  
Base Cases: one word, two words  
Regular Cases: 5 words

Time Complexity: O(n)
Space Complexity: O(n)




