class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        int n=machines.size();
        int total=0;
        for(int x:machines){
            total+=x;
        }
        if(total%n!=0){
            return -1;
        }
        int td=total/n;
        int diff,ans;
        int balance=0;
        for(int x:machines){
diff=x-td;
balance+=diff;
ans=max(ans,max(abs(balance),diff));
        }
return ans;
    }
};
