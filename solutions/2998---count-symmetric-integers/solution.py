class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans=0
        for n in range(low,high+1):
            s=str(n)
            if len(s)%2:
                continue
            m=len(s)//2
            if sum(map(int,s[:m]))==sum(map(int,s[m:])):
                ans+=1
        return ans
