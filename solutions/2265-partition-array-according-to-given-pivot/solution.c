/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    int count=0;
    int x=0,y=0;
int *a=(int*)malloc(numsSize*sizeof(int));
    int *b=(int*)malloc(numsSize*sizeof(int));
    for(int i=0;i<numsSize;i++){
        if(nums[i]<pivot){
            a[x++]=nums[i];
        }
        else if(nums[i]==pivot)
            count++;
        else
            b[y++]=nums[i];
    }
    for(int j=0;j<x;j++){
        nums[j]=a[j];
    }
    while(count!=0){
        nums[x]=pivot;
        count--;
        x++;
    }
    for(int w=x;w<x+y;w++){
        nums[w]=b[w-x];
    }
    *returnSize=numsSize;
        return nums;
    
}
