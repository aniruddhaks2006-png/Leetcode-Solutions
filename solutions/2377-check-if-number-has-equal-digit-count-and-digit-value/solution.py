class Solution:
    def digitCount(self, num: str) -> bool:
        
        d={}
        for i in range(len(num)):
            d[i]=0
        s=list(num)
        for i in s:
            if int(i) not in d:
             d[int(i)]=1
            else:
                d[int(i)]+=1
        for k in range(len(s)):
            
            if d[k]!=int(num[k]):
                return False
        return True
        
