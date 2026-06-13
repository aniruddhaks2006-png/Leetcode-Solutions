class Solution:
    def sortSentence(self, s: str) -> str:
        d={}
        s1=""
        m=s.split(" ")
        for i in m:
            d[int(i[-1])]=i[:-1]
        for v in sorted(d.keys()):
            s1+=d[v]+" "
        return s1[:-1]
            
        
