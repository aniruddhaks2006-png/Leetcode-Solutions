/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int temp=0;
    for(int i=0;i<numsSize;i++){
        nums[i]=nums[i]*nums[i];
    }
    int min=0;
    for(int j=0;j<numsSize;j++){
        min=j;
        for(int k=j;k<numsSize;k++){
            if(nums[k]<nums[min]){
                min=k;
            }
        }
        if(min!=j){
            temp=nums[j];
            nums[j]=nums[min];
                nums[min]=temp;
            
        }
        
    }
    *returnSize=numsSize;
    return nums;
}
