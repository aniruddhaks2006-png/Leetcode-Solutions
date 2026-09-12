class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        s="11"
        for i in range(n-2):
            x=""
            j=0
            while j<len(s): 
                count=1
                while j+1<len(s) and s[j]==s[j+1]:
                    count+=1
                    j+=1
                x+=str(count)+s[j]
                j+=1
            s=x
        return s
