int Max(int a ,int b){
    return (a>b)?a:b;
}
int maximumCount(int* nums, int numsSize) {
    int count1=0;
    int count2=0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]<0){
            count1++;
        }
        else if(nums[i]>0)
            count2++;
        else
            continue;
    }
    return Max(count1,count2);
}
