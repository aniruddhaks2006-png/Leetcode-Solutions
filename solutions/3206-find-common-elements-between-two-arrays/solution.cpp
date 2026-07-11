class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> a(nums1.begin(), nums1.end());
        unordered_set<int> b(nums2.begin(), nums2.end());
        
        int count1=0,count2=0;
        for(int x:nums1)
            if(b.count(x))
            count1++;
        
        for(int y:nums2){
            if(a.count(y))
            count2++;
        }
        return {count1,count2};

    }
};
