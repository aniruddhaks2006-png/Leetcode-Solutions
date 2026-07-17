class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int csum=0;
        int msum=INT_MIN;
        for(int x:nums){
            csum+=x;
            if(csum>msum)
                msum=csum;
            if(csum<0)
                csum=0;
        }
        return msum;
    }
};
