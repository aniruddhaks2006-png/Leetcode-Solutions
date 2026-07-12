int maximumScore(int*nums,int numsSize,int k){
int l=k,r=k,mn=nums[k],ans=mn;
while(l>0||r<numsSize-1){
if(l==0)
    r++;
else if(r==numsSize-1)
    l--;
else if(nums[l-1]>nums[r+1])
    l--;
else 
    r++;
int x=nums[l]<nums[r]?nums[l]:nums[r];
mn=mn<x?mn:x;
int score=mn*(r-l+1);
ans=ans>score?ans:score;
}
return ans;
}
