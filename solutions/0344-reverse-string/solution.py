class Solution:
    def reverseString(self, s: List[str]) -> None:
        x=0
        y=len(s)-1
        while x<y:
            temp=s[x]
            s[x]=s[y]
            s[y]=temp
            x+=1
            y-=1
        """
        Do not return anything, modify s in-place instead.
        """
        
