class Solution {
public:
    int findGCD(vector<int>& nums) {
        int maxi=0;
        int mini=INT_MAX;
        for(int x:nums){
            if(x<mini)
                mini=x;
            if(x>maxi)
                maxi=x;
        }
        while(mini){
            int temp=mini;
            mini=maxi%mini;
            maxi=temp;
        }
        return maxi;
    }
};
