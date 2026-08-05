class Solution{
public:
    int specialTriplets(vector<int>&nums){
        unordered_map<int,int>l,r;
        for(int x:nums)r[x]++;
        const int mod=1000000007;
        long long ans=0;
        for(int x:nums){
            r[x]--;
            ans=(ans+1LL*l[x*2]*r[x*2])%mod;
            l[x]++;
        }
        return ans;
    }
};
