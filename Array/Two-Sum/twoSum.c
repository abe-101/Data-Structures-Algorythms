/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *indices = malloc(2*sizeof(indices));
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[j] + nums[i] == target) {
                indices[0] = i;
                indices[1] = j;
            }
        }
    }
    *returnSize = 2;
    return indices;
}
