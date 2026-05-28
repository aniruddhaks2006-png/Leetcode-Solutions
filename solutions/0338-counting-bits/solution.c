/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    int *arr=(int*)malloc((n+1)*sizeof(int));
    int x=0,count=0;
    *returnSize=n+1;
    for(int i=0;i<n+1;i++)
    {x=i;
     count=0;
        while(x!=0)
        {
            count++;
            x=x&(x-1);
        }
     arr[i]=count;
    }
   return  arr; 
}
