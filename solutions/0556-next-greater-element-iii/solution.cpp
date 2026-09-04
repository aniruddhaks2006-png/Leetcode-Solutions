#include <bits/stdc++.h>
class Solution {
public:
    int nextGreaterElement(int n) {
        vector<int> a;
        int x=n;
    while(n!=0){
        a.push_back(n%10);
        n/=10;
    }
        reverse(a.begin(),a.end());
        long long n1=0;
        next_permutation(a.begin(),a.end());
       for(int y:a){
           n1=n1*10+y;
       }
        if(n1>INT_MAX || n1<=x){
            return -1;
        }
        return n1;
    }
};
