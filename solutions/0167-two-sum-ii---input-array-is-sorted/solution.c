/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int low=0,mid=0,count=0;
    int *n=numbers;
    int high=numbersSize-1;
    while(low<high){
        if(n[low]+n[high]==target)
        { count=1;
            break;
        }
        else if (n[low]+n[high]>target)
        {
           high--;
        }
        else
          low++;
          
    
    }
    int *a=(int*)malloc(2*sizeof(int));
          *returnSize=2;
    if(count>0){
        a[0]=low+1;
        a[1]=high+1;

    
    
    return a;    
    } 
     a[0]=-1;
     a[1]=-1;
     return a;
}
    
    

