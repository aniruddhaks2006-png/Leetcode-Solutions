int maxAdjacentDistance(int* nums, int numsSize) {
    int max = abs(nums[0] - nums[numsSize - 1]);

    for (int i = 1; i < numsSize; i++) {
        int diff = abs(nums[i] - nums[i - 1]);
        if (diff > max) {
            max = diff;
        }
    }

    return max;
}
