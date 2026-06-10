/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParityII(int* nums, int numsSize, int* returnSize) {
    int *a=(int*)malloc(numsSize*sizeof(int));
    int k=0;
    int f=1;
    for(int i=0;i<numsSize;i++){
        if(nums[i]%2==0){
            a[k]=nums[i];
            k=k+2;
        }
        else{
            a[f]=nums[i];
            f=f+2;
        }
    }
    *returnSize=numsSize;
    return a;
}
