int maxSubarrays(int* nums, int numsSize) {
    int total = nums[0];
    for (int i = 1; i < numsSize; i++)
        total &= nums[i];
    if (total!=0)
        return 1;
    int ans=0;
    int curr=~0;
    for (int i = 0; i < numsSize;i++) {
        curr &= nums[i];
        if (curr == 0) {
            ans++;
            curr = ~0;
        }
    }
    return ans;
}
