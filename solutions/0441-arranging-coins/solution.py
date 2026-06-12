class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        sum=0
        while sum<=n:
            sum+=i
            if sum==n:
                return i
            elif sum<n:
                i+=1
                continue
            else:
                return i-1
        
