class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        m[0]=-1;
int sum=0;
int rem;
        for(int i=0;i<nums.size();i++){
            sum=sum+nums[i];
            rem=sum%k;
            if(m.count(rem)){
                if(i-m[rem]>=2)
            return true;
            }
            else
            m[rem]=i;
            
            
        }
            return false;
    }
};
