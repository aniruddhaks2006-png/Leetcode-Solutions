class Solution:
    def reverseWords(self, s: str) -> str:
       l=0
       r=0
       s=list(s)
       p=""
       while r<len(s):
           if s[r]==" ":
                s[l:r]=s[l:r][::-1]
                l=r+1
                r=l
           r+=1
           if r==len(s)-1:
                s[l:r+1]=s[l:r+1][::-1]
                break
       for i in s:
             p+=i
       return p
                
             
      
