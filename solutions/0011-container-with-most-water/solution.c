int min(int a, int b){
    if(a < b)
        return a;
    return b;
}

int maxArea(int* height, int heightSize) {
    int left = 0;
    int right = heightSize - 1;
    int area = 0, maxarea = 0;

    while(left < right){
        area = min(height[left], height[right]) * (right - left);

        if(area > maxarea)
            maxarea = area;

        if(height[left] > height[right])
            right--;
        else
            left++;
    }

    return maxarea;
}
