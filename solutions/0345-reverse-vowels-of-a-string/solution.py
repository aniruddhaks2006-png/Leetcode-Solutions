class Solution:
    def reverseVowels(self, s1: str) -> str: 
        s=list(s1)
        x=0
        y=len(s)-1
        while x<y:
            if s[x] not in "aeiouAEIOU":
                x+=1
            elif s[y] not in "aeiouAEIOU":
                y-=1
            else:
                temp=s[x]
                s[x]=s[y]
                s[y]=temp
                x+=1
                y-=1
        s2=""
        for i in s:
            s2+=i
        return s2
