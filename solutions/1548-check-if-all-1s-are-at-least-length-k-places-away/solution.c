bool kLengthApart(int* nums, int numsSize, int k) {
    int left=0,right=0;;
    while(left<numsSize){
        if(nums[left]==1){
            break;
        
        }
        left++;
    }
    right=left;
    while(right<numsSize){
        if(nums[right]==1){
            if(k>=right-left && left!=right)
            return false;
            left=right;
        }
        right++;
    }
    return true;
}
