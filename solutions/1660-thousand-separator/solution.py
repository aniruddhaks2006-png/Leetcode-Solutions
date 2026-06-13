class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)
        if len(s)<=3:
            return s
        x=3
        while len(s)-x>0:
           pos = len(s)-x
           s= s[:pos] + "." + s[pos:]
           x+=4
          
        return s

