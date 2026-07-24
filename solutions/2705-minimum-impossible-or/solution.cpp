class Solution {
public:
    int minImpossibleOR(vector<int>& nums) {
        unordered_set<int> a(nums.begin(),nums.end());
        int ans=1;
        while(a.count(ans)){
            ans<<=1;
        }
        return ans;
    }
};
