int singleNumber(int* nums, int numsSize) {
    int temp=0,min;
    for(int i=0;i<numsSize;i++){
        min=i;
        for(int j=i+1;j<numsSize;j++)
        {
            if(nums[min]>nums[j])
            { 
                min=j;
            }
        }
            if(min!=i)
            {
               temp= nums[min];
                nums[min]=nums[i];
                nums[i]=temp;
            }
        }
    
            for (int g=0;g<numsSize;g+=2)
            {
                if(g==numsSize-1)
                    return nums[g];
                if(nums[g]!=nums[g+1])
                    return nums[g];
            }
            
            
        
    
    return 0;
}
