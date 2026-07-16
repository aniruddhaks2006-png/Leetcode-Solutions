class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> si;
        si.push(-1);
        int maxl=0;
        int diff=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='(')
                si.emplace(i);
            else{
                si.pop();
                if(si.empty())
                    si.push(i);
                else{
                diff=i-si.top();
                maxl=max(maxl,diff);
                }
                
        }
        
    }
        return maxl;
    }
};
