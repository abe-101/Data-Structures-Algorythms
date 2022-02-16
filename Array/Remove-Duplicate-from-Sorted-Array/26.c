#include <stdio.h> 

int removeDuplicates(int* nums, int numsSize){
    if (numsSize == 0)
        return 0;

    int count = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[count] != nums[i]){
            nums[++count] = nums[i];
        }
    }
    return count + 1;
}
