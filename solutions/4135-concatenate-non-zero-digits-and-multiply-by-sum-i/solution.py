class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        sum=0
        s=s.replace("0","")
        if(s):
         for i in s:
            sum+=int(i)
        
         return int(s)*sum
        else:
            return 0

        
        
