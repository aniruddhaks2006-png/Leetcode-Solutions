class Solution:
    def reverseWords(self, s: str) -> str:
        m=s.split()
        str2=""
        x=len(m)
        for i in range(x):
            if(i!=x-1):
             str2+=m[x-1-i]+" "
            else:
                str2+=m[x-1-i]
        return str2
        
