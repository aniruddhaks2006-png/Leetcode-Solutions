int getMaxDigit(int num) {
    int mx = 0;
    while (num > 0) {
        if (num % 10 > mx)
            mx = num % 10;
        num /= 10;
    }
    return mx;
}
int maxSum(int* nums, int numsSize) {
    int largest[10];
    for (int i = 0; i < 10; i++)
        largest[i] = -1;
    int ans = -1;

    for (int i = 0; i < numsSize; i++) {
        int digit = getMaxDigit(nums[i]);

        if (largest[digit] != -1) {
            int sum = largest[digit] + nums[i];
            if (sum > ans)
                ans = sum;
        }
        if (nums[i] > largest[digit])
            largest[digit] = nums[i];
    }
    return ans;
}
