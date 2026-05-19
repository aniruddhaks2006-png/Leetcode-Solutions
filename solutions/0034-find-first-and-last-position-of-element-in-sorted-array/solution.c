/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int first=-1;
    int last=-1;
    int count=0;
    int *num=(int*)malloc(2*sizeof(int));

    for(int i=0;i<numsSize;i++)
    {
        if(count<1 && nums[i]==target)

        {
            first=i;
            last=i;
            count++;
        }
        else if(count=1 && nums[i]==target)
        {
          while(nums[i]!=target)
          {
            i++;
            
          }
          last=i;
        }
    }
    num[0]=first;
    num[1]=last;
    *returnSize=2 ;
    return num;
}
