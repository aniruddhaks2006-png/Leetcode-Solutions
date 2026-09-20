class Solution {
public:
    int reverseDegree(string s) {
        int sumi=0;
        for(int i=0;i<s.size();i++){
            sumi+=(26-(s[i]-'a'))*(i+1);
        }
        return sumi;
    }
};
