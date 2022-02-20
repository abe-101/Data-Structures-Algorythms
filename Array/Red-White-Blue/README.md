## Red, White and Blue

**Level**: Medium

Note: This solution uses Enums and Exceptions. While optional, it always looks good if you use them in an
interview.
You're given a list of Marbles. Each marble can have one of 3 colors (Red, White or Blue).
Arrange the marbles in order of the colors (Red -> White -> Blue).
Colors are represented as follows:
0 - Red
1 - White
2 - Blue


Questions to Clarify:  
Q. Waht to do with an unknown input type?  
A. Throw an exception  

Q. How should the answer be returned?  
A. Move around in the array.  

## Solution

Same solution with Dutch National Flag. using two pointers one tracking low_boundary and one tracking high_boundary.

**Pseudocode**:
```
low_boundary = 0, high_boundary = a.length -1
i = 0

while i <= high_boundary
    if a[i].color is RED:
        add a[i] to low boundary and expand boundary by 1
        i++
    else if a[i].color is BLUE
        add a[i] to high boundary and expand boundary by 1
        don't increment i because the current i needs to be processed
                as it came from ahead
    else if a[i].color is WHITE
        i++
    else
        throw exeption

```
**Test Cases**:
Edge Cases: empty array, null array, invalid color  
Base Cases: single element, two elements  
Regular Cases: list has element with - all 3 colors, only 2 colors, only 1 color  

Time Complexity: O(n)

Space Complexity: O(1)





