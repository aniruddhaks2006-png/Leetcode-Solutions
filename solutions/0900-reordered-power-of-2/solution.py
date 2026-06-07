class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        x=str(n)
        l=len(x)
        g=[]
        f=0
        m=2**f
        while len(str(m))<=l:
            if len(str(m))==l:
                g.append(str(m))
            f+=1
            m=2**f
        for i in g:
            if(sorted(x)==sorted(i)):
                return True
        return False
        
