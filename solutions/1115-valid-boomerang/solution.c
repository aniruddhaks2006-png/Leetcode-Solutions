bool isBoomerang(int** nums, int pointsSize, int* pointsColSize) {
    return (nums[1][1]-nums[0][1])*(nums[2][0]-nums[0][0])!=(nums[2][1]-nums[0][1])*(nums[1][0]-nums[0][0]);
}
